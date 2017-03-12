from fabric.api import local
from fabric.api import env
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.context_managers import env

env.hosts = ['john@10.211.55.11']
env.passwords = {
    "john@10.211.55.11:22":"12345678"
}
def push():
   rsync_project(local_dir='./', remote_dir='~/AmazonPioT/')
   #run('/etc/init.d/init restart ')
   with cd('~/AmazonPioT/sdk/samples/linux/subscribe_publish_cpp_sample/'):
       run("make TARGET=linux all subscribe_publish_cpp_sample")    
def deploy():
    commit()
    push()
