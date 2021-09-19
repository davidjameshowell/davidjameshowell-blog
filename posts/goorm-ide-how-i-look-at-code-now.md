Goorm IDE - How I look at code now|Code whenever, wherever. Deploy however. Containerized instances for development.
# Goorm IDE - How I look at code now

## Preface

I don't consider myself a web dev or developer by any stretch of the imagination. However, I love making functional based apps (and leaning heavily on Bootstrap becuase I'm not creative) usually with Python. If I'm working locally, I'm usually using VSCode due to integrations and how pretty it is. But I do transition between a lot of customers and sometimes they either are not properly setup for development or the time between needing to commit and pull down a repo is too much.

In the past, way before Amazon acquired them, Cloud9 was my go to repo. I have since explored them, along with many others like Eclipse Che, VSCode for Docker, as well as some others that connects to infra. While a lot of these do solve the issue of remote coding, I never felt like they were easy to use. Knowing me, I like to self host a lot of items, but if someone can do it better and for free, they have my vote.

## Enter new contender - Goorm IDE

Goorm IDE, a Korean company, offers a SaaS model type similar to the original Cloud9 model (also using Amazon).

[![Goorm IDE Plans](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/haBiBoCe82.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/haBiBoCe82.png/raw)

My favorite thing about Goorm IDE is the fact that you are provided with a container in which to store as well as install whatever software you may need (minus virtualization, such as Docker). The free tier providers up to 5 containers however you want to slice it, 10GB per container, and 10GB of storage per container.

[![Goorm IDE Containers](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/SIzINEZI65.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/SIzINEZI65.png/raw)

As you can see by the above, I currently have 3 containers (or projects). One is all of my Zappa projects, one is a utilities container I was using as scriptland, and the last one was around Sonarr imports for large libraries from cloud storage. I still have access to create two more containers 

[![Goorm IDE Create Containers](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/gaFEQujU36.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/gaFEQujU36.png/raw)


## The Interface

From the create option, there are a pleathora of options that we can enable including making a public private project, what region as well as additional utilities to include.


[![Goorm IDE Interface](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/YAlISAYA81.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/YAlISAYA81.png/raw)

The interface is exactly everything I was looking for. There are a TON of options you can choose from, including splitting windows and rendering files (such as the one in this screenshot above as I was writing this). It will render Markdown for me inline so I can view as I write without needing another extra IDE.

Below there is terminal that operates just as any Linux terminal would. Since it is running in a container, there is not init system to keep in mind. To the top right there are build, test, and run commands. I have selected the build commands I have which automatically go into the selected top level folder, source my virtualenv, and run a zappa update or deploy as appropriate to send my packages out to AWS.

The typing interface is great and does highlighting for many languages, Python included. I find it extremely helpful and mimics similar conventions to what you would expect from VSCode.

[![Goorm IDE Interface](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/hUCeguhe29.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/hUCeguhe29.png/raw)

The far left does file management and has a host of options to choose from including import and export of files (read: upload and downloading), renaming, moving building files/testing files from configurations. 

[![Goorm IDE Interface](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/PUwaFEzu25.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/PUwaFEzu25.png/raw)

Sometimes you might be limited on screen real-estate or want to run a command inside the terminal while maximizing the code window. You can do that too! With Container > SSH configuration, you can setup a one time [SSH configuration](https://help.goorm.io/en/goormide/17.various-features/ssh-port-forwarding#ssh) to be used for the duration that the workspace is available. I use this when I am on my laptop since I have DPI set to about 200% which makes items very easy to touch, but reduces my screen size a significant chunk.

[![Goorm IDE SSH Configuration](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/fajuVayo60.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/fajuVayo60.png/raw)

# Deployments

Now, I know you probably think I may be the anti-pattern to devops, with no solid deployment releases for Zappa based projects. However, in my defense, given the very low technical overhead requirements, a continous deployment process for this would be overkill.

**Enter Build and Run commands**

As shown in the interface screen, I have a drop-down panel which lists Deploy Dev, Deploy Prod, Update Dev, Update Prod, and add a build command. Since I am using a Zappa based environment, I utilize the build to push the code up to S3 for deployments to both production and development releases. I have these set so that I select the top level folder of the project, select Deploy or Update the environment, and it will begin the process.

It runs a cd on the selected folder, sources the VirtualEnv, and then runs either zappa deploy or zappa update <env>.

[![Goorm IDE Build Commands](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/XuWeTUSu99.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/XuWeTUSu99.png/raw)

It is simple, fast, and will the build in a new tab below (where the terminal is) that afterwards can simply be closed.

## Closing Remarks

The Team behind Goorm is very friendly and responds to inquiries in a speedy  fashion. A localisation bug was resolved within 24 hours involving the name "taps" to be changed to the proper name of "tabs" for right clicking and removing the above tabs seen.

But the best by far is the portability of Goorm. I can take it where I go, test where ever, and make changes whenever. For that fact alone, Goorm has my cotninued support and dedication.

### Remarks worth mentioning

This blog article was recently/is currently featured on Goorm's new container redesign (which by the way is awesome and slick!). 

[![Goorm IDE Featured Article](https://images.weserv.nl/?url=https://images.djh-projects.com/lumu5/YOMASUnu02.png/raw?fit=inside&height=350)](https://images.djh-projects.com/lumu5/YOMASUnu02.png/raw)

As a result, I did receive a coupon (unsolicited) from Goorm for premium service for three months. I graciously appreciate Goorm's continued support and commitment to user support, along with the encouragement in writing this article. With that said, all the opinions about Goorm and praise are my own opinions and were not influenced in any way.

~David
