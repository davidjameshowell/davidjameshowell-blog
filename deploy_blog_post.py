import sqlite3
from sqlite3 import Error
import time

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def select_post_from_slug(conn, slug):
    cur = conn.cursor()
    cur.execute("SELECT content_hash FROM post WHERE slug = ?", (slug,))
    row = cur.fetchone()
    return row

def get_file_contents(filename):
    file_contents = ""
    with open(filename, "r") as f:
        file_contents = f.readlines()
    return file_contents

def get_post_content(file_contents):
    out_str = " "
    return out_str.join(file_contents[1:])

def get_post_headers(file_contents):
    return file_contents[0].split('|')

def add_new_blog_post(conn, filename, slug, content_hash):
    file_contents = ""
    post_contents = ""
    file_contents = get_file_contents(filename)
    post_contents = get_post_content(file_contents)
    post_headers = get_post_headers(file_contents)
    created_on = int(time.time())
    
    sql = ''' INSERT INTO post(content,slug,content_hash,title,subtitle,created_on)
              VALUES(?,?,?,?,?,?) '''
    sql_values = (post_contents, slug, content_hash, post_headers[0], post_headers[1], created_on)

    cur = conn.cursor()
    cur.execute(sql, sql_values)
    conn.commit()

    return cur.lastrowid
        
def update_blog_post(conn, filename, slug, content_hash):
    file_contents = get_file_contents(filename)
    post_contents = get_post_content(file_contents)
    post_headers = get_post_headers(file_contents)
    
    sql = ''' UPDATE post SET content = ?, content_hash = ?, title = ?, subtitle = ?
              WHERE slug = ? '''
    sql_values = (post_contents, content_hash, post_headers[0], post_headers[1], slug)

    cur = conn.cursor()
    cur.execute(sql, sql_values)
    conn.commit()
    return cur.lastrowid

def grab_local_post_files():
    import glob
    return glob.glob("./posts/*.md")
    
def get_md5_of_local_post_file(filename):
    import hashlib
    file_md5 = hashlib.md5(open(filename,'rb').read()).hexdigest()
    return file_md5
    
if __name__ == '__main__':
    conn = create_connection(r"./blog_db/blog.db")
    local_post_files = grab_local_post_files()
    
    post_listings = []
    for file in local_post_files:
        slug = file[8:-3]
        md5hash = get_md5_of_local_post_file(file)
        post_listings.append({"slug": slug, "hash": md5hash})
        
        post_lookup = select_post_from_slug(conn, slug)
        
        if post_lookup is None:
            print("Adding new blog post for {slug} - {md5hash}".format(slug=slug, md5hash=md5hash))
            add_new_blog_post(conn, file, slug, md5hash)
        elif post_lookup[0] != md5hash:
            print("Updating blog post for {slug} - {md5hash}".format(slug=slug, md5hash=md5hash))
            update_blog_post(conn, file, slug, md5hash)
