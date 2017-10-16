# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re


cl = LINETCR.LINE()
cl.login(token="ElRZ0ZKFqP0I9BTtYcX1.VogNe+dnaFO7qc69pNlSSq.kNVUL0WTrDL4lvQ2D5nfBB3lXj85wUg2BiGUYVvmrHc=")

ki = LINETCR.LINE()
ki.login(token="ElB2Pep3wDGCaBWDOHOd.rHYNqNhooMO2AAix7FG/dq.FT8LKaCO3YRqNNBffRTEvmZNVFlZjngRMJjVE/ayes0=")

kk = LINETCR.LINE()
kk.login(token="El5EGr8JsO1JIeIVAiKd.zwEkdQNuUNYWLmtDouRyJq.MhoFA71PHJW9nkpWT5sUPRLWHcDOsLo5OJLb+ilYUQc=")

kc = LINETCR.LINE()
kc.login(token="ElRNGwYuTGRVrmUIcF8d.C/VdWfYFmMyZ1YcBQL5kxq.+4lClC1Jmktw//hL7sRPbZQhGzKexmv1VJKh+egzoJw=")

kl = LINETCR.LINE()
kl.login(token="ElDKAF8uQmpLW6tkzC0e.0oz4ZwAHo3Bvivjx8lNH3G.FGrEztgfBHMktEZlqt622+8guARvCUtQkG/PhW1CdlA=")

kj = LINETCR.LINE()
kj.login(token="ElOBpkNH8MYWP65GwfQ1.XKW3EohLM2icd/jlaiAhmq.810nSy0KfSVcjKVAAObpPgv/pBMjh5ZNDQ5ttkxVbDc=")

kh = LINETCR.LINE()
kh.login(token="El2WH13qTSjngBBzObBe.e5lgC5+i1Bh15zl4/OzzdG.9UR0+H2qeiNzS39f2vcRKelGuG8j+ZQvSN4J8/gn/rg=")

ka = LINETCR.LINE()
ka.login(token="El0RjCgVo9b4N3dTRlNc.V4KVh/U3ay0fhsDBqCxbVa.XD7ZSXKsHm3wLFspwUOa5En8a6B/IXsCA26C+4Aahro=")

kz = LINETCR.LINE()
kz.login(token="ElZC5QFbnWiqqqqY26Z1.niGNQ6hxoZL8fNYyR6PYuq.PiL5kt5xqJYtucPH+80Zt3csjOijfwV2QxeBpSqETxw=")

ks = LINETCR.LINE()
ks.login(token="ElN1CqFFIvod4aMVjNx6.fZ6Oit60RnHeCLKcjobFzG.pdONe/NvD5GwM2QCyoVUP3K/IkY9Ee/XerBhCY9fhZ8=")

kb = LINETCR.LINE()
kb.login(token="Eljlfo9aPkUYOw3DPPV4.Z/KYWQ4jucOEPlEi6sn7ra.PZr8/vBLn51Mqgf2mDqGQHCdDa7fGbom34xG0HBWuV8=")

kw = LINETCR.LINE()
kw.login(token="ElKa57Tu24Wlowu2ENn0.PQVf82HpryeddPW9tbCmma.JXqoktQZpbBih84DsjNhY36RAnbcg1fbCMLx8dxNzaA=")

nl = LINETCR.LINE()
nl.login(token="EltqQlWZCtXcl0x9Mkk4.6OowBXq+Jy0nf7bEbCA0ba.190oTjN9CarVKARxtr26r4n3c+tpW1yJUXq1DzzQyxw=")

#ak = LINETCR.LINE()
#ak.login(token="")


#ak = cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ↳卐ł₳₦™ ฿☫₮✒✈↰

❅[Bot all/Ian?]
❅[Bot cancel/Ian cancel]
❅[Ginfo]
❅[Gid]
❅[Jam on]
❅[List group]
❅[/ListIDGroup]
❅[Mid「@Target」]
❅[Adminlist/Admin lis]
❅[Sttafflist/Staff lis]
❅[Creator]
❅[Gcreator:inv]
❅[Change clock]
❅[Jam update/Update]
❅[Setp]
❅[Cek]
❅[Kuy join/Ayo masuk]
❅[Bye all/Babay]
❅[Mentionall]
❅[Respon]
❅[Sp/Speed]
❅[Speed all/Sp all]
❅[Ginfo]
❅[Next Key 「Helpp/Keyy」]

✎Support by 『卐ł₳₦™☤』
☎My Creator Http://line.me/ti/p/~lianekof
"""

Setgroup =""" ↱prιvαтe coммαɴd↲

✎[Gn 「NamaGroup」]
✎[Ourl/Oqr]
✎[Curl/Cqr]
✎[TL:「Text」]
✎[Cn 「Name」]
✎[Message change:「Text」]
✎[Message add:「Text」]
✎[Group bc「Text」]
✎[Contact bc「Text」]
✎[Copy「@Target」]
✎[Name「@Target」]
✎[Bl「@Target」]
✎[Wl「@Target」]
✎[Kill「@Target」]
✎[Admin add「@Target」]
✎[Admin remove「@Target」]
✎[/AcceptInvitation:「Gid」]
✎[/AcceptAllInvitation]
✎[/CancelInvited:「Gid」]
✎[Setting]

✎Support by 『卐ł₳₦™☤』
☎My Creator Http://line.me/ti/p/~lianekof
"""
KAC=[cl,ki,kk,kc,kl,kj,kh,ka,kz,ks,kb,kw,nl]
KIL=[ki,kk,kc,kl,kj,kh,ka,kz,ks,kb,kw,nl]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kl.getProfile().mid
Emid = kj.getProfile().mid
Fmid = kh.getProfile().mid
Gmid = ka.getProfile().mid
Hmid = kz.getProfile().mid
Imid = ks.getProfile().mid
Jmid = kb.getProfile().mid
Kmid = kw.getProfile().mid
Lmid = nl.getProfile().mid
Mmid = nl.getProfile().mid


Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,"ubce1a713f0cd01fa3b402ebd3e72ecb1"]
admin=["ubce1a713f0cd01fa3b402ebd3e72ecb1","uea83966f143f8d8d0d17b05e05c6b404",]
creator=["ubce1a713f0cd01fa3b402ebd3e72ecb1"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"Thanks for add me,My Creator Http://line.me/ti/p/~lianekof",
    "lang":"JP",
    "comment":"Thanks for add me,My Creator Http://line.me/ti/p/~lianekof",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"‮ ™NaI🚀",
    "cName2":"Tsuna",
    "cName3":"Laxus",
    "cName4":"Natsu",
    "cName5":"Yatogami",
    "cName6":"Sasuke",
    "cName7":"Itachi",
    "cName8":"Yahiko",
    "cName9":"Shirou",
    "cName10":"Kaneki",
    "cName11":"Wolf Police",
    "cName12":"Lord Angel",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":False,
    "Protectguest":False,
    "Protectjoin":False,
    "Protectcancel":False,
    "protection":True,
    "atjointicket":True,
    "welcome":False,
    "winvite":False,
    "autolike":False,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage 
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.type == 55:        
         if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass             



#def autolike():    
#     for zx in range(0,20):
#        hasil = cl.activity(limit=20)
#        if wait["autolike"] == True:
#         if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#          try:    
#            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            kl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            kj.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kj.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            kh.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kh.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            kz.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kz.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kb.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            kw.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            kw.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by IaN™ Http://line.me/ti/p/~lianekof")
#            print "Like"
#          except:
#            pass
#        else:
#            print "Already Liked"
#     time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                ki.findAndAddContactsByMid(op.param1)
                kc.findAndAddContactsByMid(op.param1)
                kk.findAndAddContactsByMid(op.param1)
                kl.findAndAddContactsByMid(op.param1)
                kj.findAndAddContactsByMid(op.param1)
                kh.findAndAddContactsByMid(op.param1)
                ka.findAndAddContactsByMid(op.param1)
                kz.findAndAddContactsByMid(op.param1)
                ks.findAndAddContactsByMid(op.param1)
                kb.findAndAddContactsByMid(op.param1)
                kw.findAndAddContactsByMid(op.param1)
                
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    ki.sendText(op.param1,str(wait["message"]))
                    kc.sendText(op.param1,str(wait["message"]))
                    kk.sendText(op.param1,str(wait["message"]))
                    kl.sendText(op.param1,str(wait["message"]))
                    kj.sendText(op.param1,str(wait["message"]))
                    kh.sendText(op.param1,str(wait["message"]))
                    ka.sendText(op.param1,str(wait["message"]))
                    kz.sendText(op.param1,str(wait["message"]))
                    ks.sendText(op.param1,str(wait["message"]))
                    kb.sendText(op.param1,str(wait["message"]))
                    kw.sendText(op.param1,str(wait["message"]))

        #------Open QR Kick start------#
        if op.type == 11:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   klist=[cl,ki,kk,kc,kl,kj,kh,ka,kz,ks,kb,kw]
                   kicker=random.choice(klist)
                   kicker.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        if op.type == 11:
            if op.param2 not in Bots:
                return
            random.choice(KIL).sendText(op.param1,"Jangan Main Qr Goblog " + cl.getContact(op.param2).displayName)
            print "Update group"                   

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KIL).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#
        #------------------------------------Kick Auto Bl start------------------------------------#				
	if op.type == 19:
             if not op.param2 in admin and Bots:
                 try:
                     gs = ki.getGroup(op.param1)
                     gs = random.choice(KIL).getGroup(op.param1)
                     targets = [op.param2]
                     for target in targets:
                        try:
                             wait["blacklist"][target] = True
                             f=codecs.open('st2__b.json','w','utf-8')
                             json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        except:
                         return


                 except Exception, e:
                     print e
        #--------------------------------Kick Auto Bl Done----------------------------------#
                  
        #------Joined User Kick start------#
        if op.type == 17:
           if wait["Protectjoin"] == True:
               if op.param2 not in Bots:
                   random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
               
        #------Joined User Kick start------#
        #------Joined Sambut Start------#				
        if op.type == 17:
           if wait["welcome"] == True: 
            if op.param2 in Bots:
                return
            ginfo = cl.getGroup(op.param1)
            cl.sendText(op.param1, "Welcome To " + str(ginfo.name) + displayName)
            cl.sendText(op.param1, "Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
            print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if op.param2 in Bots:
                return
            random.choice(KIL).sendText(op.param1, "Sayonara Kaka" + displayName)
            print "MEMBER HAS LEFT THE GROUP"                   
        #------Joined Sambut Done------#

        #-------------------------Kick Auto Bl Start--------------------#
        if op.type == 11:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = random.choice(KIL).getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return


                    except Exception, e:
                        print e
        #-------------------------Kick Auto Bl Done--------------------#
        #-------------------------Kick Bl Join Start--------------------#
        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace(".",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])            
        #-------------------------Kick Bl Join Done--------------------#            
        #------ User Kick start------#
        if op.type == 19:
           if wait["protection"] == True:
               if op.param2 not in Bots:                  
                  random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
        #------ User Kick Finish------#                  

        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Dmid:
                if op.param2 in Emid:
                    X = kl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kl.reissueGroupTicket(op.param1)

            if op.param3 in Emid:
                if op.param2 in Fmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)

            if op.param3 in Fmid:
                if op.param2 in Gmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Gmid:
                if op.param2 in Hmid:
                    X = kw.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kw.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kw.reissueGroupTicket(op.param1)

            if op.param3 in Hmid:
                if op.param2 in Imid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Imid:
                if op.param2 in Jmid:
                    X = kj.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kj.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kj.reissueGroupTicket(op.param1)

            if op.param3 in Jmid:
                if op.param2 in Kmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Kmid:
                if op.param2 in mid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)                    

            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    
            if op.param3 in Lmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)                   

            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                cl.updateGroup(X)
                Ti = cl.reissueGroupTicket(op.param1)
    #===============Auto Join =====================#
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:                            
                            cl.rejectGroupInvitation(op.param1)                            
                        else:
                            cl.acceptGroupInvitation(op.param1)                            
                    else:
                        cl.acceptGroupInvitation(op.param1)                        
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)                        
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    random.choice(KIL).cancelGroupInvitation(op.param1,[op.param2])

    #===============Auto Join =====================#
         

        if op.type == 19:
         if wait["protection"] == True:   
           if op.param2 not in Bots:
              random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KIL).inviteIntoGroup(op.param1,[op.param2],admin,Bots)
              acceptGroupInvitation(op.param1,[op.param2],admin,Bots)

        if op.type == 19:
          if wait["protection"] == True:  
           if op.param2 not in Bots:
              ki.kickoutFromGroup(op.param1,[op.param2])
              ki.inviteIntoGroup(op.param1,[op.param2],admin,Bots) 
              random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KIL).inviteIntoGroup(op.param1,[op.param2],admin,Bots)              
           else:
               pass

        if op.type == 19:            
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



        if op.type == 19:            
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 19:            
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



        if op.type == 19:            
                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



        if op.type == 19:            
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kw.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kw.updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



        if op.type == 19:            
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



        if op.type == 19:            
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



        if op.type == 19:            
                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True




        if op.type == 19:            
                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



        if op.type == 19:            
                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True




        if op.type == 19:            
                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3],Bots)
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



        if op.type == 19:            
                if Kmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KIL).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KIL).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kj.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kz.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    kw.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:                            
                            kl.rejectGroupInvitation(op.param1)                                                        
                        else:
                            kl.acceptGroupInvitation(op.param1)                            
                    else:
                        kl.acceptGroupInvitation(op.param1)                        
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message

        #------Cancel User Kick start------#
        if op.type == 32:
           if wait["Protectcancel"] == True: 
            if op.param2 not in Bots:
                klist=[cl,ki,kk,kc,kl,kj,kh,ka,kz,ks,kb,kw]
                kicker=random.choice(klist)
                kicker.kickoutFromGroup(op.param1,[op.param2])
        #-----Cancel User Kick Finish------#

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        random.choice(KIL).sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        random.choice(KIL).sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        random.choice(KIL).sendText(msg.to,"Done Hapus")                        
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        random.choice(KIL).sendText(msg.to,"Tidak Ada Blacklist")                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        random.choice(KIL).sendText(msg.to,"Sudah Terbanned")                        
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        random.choice(KIL).sendText(msg.to,"Done")                        

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        random.choice(KIL).sendText(msg.to,"Done Hapus")                        
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        random.choice(KIL).sendText(msg.to,"Tidak Ada Blacklist")                        
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Keyy","Helpp"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("LA gn " in msg.text):
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("LA gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot gn " in msg.text):
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = random.choice(KIL).getGroup(msg.to)
                    X.name = msg.text.replace("WP gn ","")
                    random.choice(KIL).updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Natsu gn " in msg.text):
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Natsu gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "LA kick " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("LA kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "WP kick " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("WP kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Natsu kick " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("Natsu kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite: " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "LA invite " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("LA invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "WP invite " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("WP invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Natsu invite " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("Natsu invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Bot all","Bot all","Ian?"]:
               if msg.from_ in admin: 
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                kj.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kh.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ka.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                kz.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ks.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                kb.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Kmid}
                kw.sendMessage(msg)
            elif msg.text in ["LA"]:
               if msg.from_ in admin: 
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["WP"]:
               if msg.from_ in admin: 
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["Ian"]:
               if msg.from_ in admin: 
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Yatogami"]:
               if msg.from_ in admin: 
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kl.sendMessage(msg)
            elif msg.text in ["Natsu"]:
               if msg.from_ in admin: 
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)                
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
               if msg.from_ in admin: 
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'f44b6a1a-bdfa-47f7-a839-e7938eb71aac',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","LA gift"]:
               if msg.from_ in admin: 
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '749ecd23-e038-4cd5-acac-23d46f4277c8',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","WP gift"]:
               if msg.from_ in admin: 
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Natsu gift"]:
               if msg.from_ in admin: 
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '291e428d-e003-4d89-b8b2-a3e720fa11e0',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
               if msg.from_ in admin: 
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '749ecd23-e038-4cd5-acac-23d46f4277c8',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak Ada yang Bisa Dicancel")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot cancel","Ian cancel"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    G = random.choice(KIL).getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        random.choice(KIL).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            random.choice(KIL).sendText(msg.to,"Tidak Ada yang Bisa Dicancel")
                        else:
                            random.choice(KIL).sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KIL).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KIL).sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open Url","Ourl"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["LA ourl","LA link on"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Bosq")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["WP ourl","WP link on"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Bosq")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Oqr","Open qr"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KIL).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KIL).sendText(msg.to,"Done Bosq")
                    else:
                        random.choice(KIL).sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KIL).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KIL).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close Url","Curl"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link Close")
                    else:
                        cl.sendText(msg.to,"Already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["LA curl","LA link off"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Bosq")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["WP curl","WP link off"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Bosq")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cqr","Close qr"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KIL).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KIL).sendText(msg.to,"Done Bosq")
                    else:
                        random.choice(KIL).sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KIL).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KIL).sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				ki.acceptGroupInvitationByTicket(group.mid,ticket_id)
				kk.acceptGroupInvitationByTicket(group.mid,ticket_id)
				kc.acceptGroupInvitationByTicket(group.mid,ticket_id)
				kl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
               if msg.from_ in admin: 
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Gid" == msg.text:
               if msg.from_ in admin: 
                kk.sendText(msg.to,msg.to)
            elif "IaN" == msg.text:
               if msg.from_ in admin: 
                cl.sendText(msg.to,mid)
            elif "LA" == msg.text:
               if msg.from_ in admin: 
                ki.sendText(msg.to,Amid)
            elif "WP" == msg.text:
               if msg.from_ in admin: 
                kk.sendText(msg.to,Bmid)
            elif "Natsu" == msg.text:
               if msg.from_ in admin: 
                kc.sendText(msg.to,Cmid)
            elif "Yatogami" == msg.text:
               if msg.from_ in admin: 
                kl.sendText(msg.to,Dmid)                
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                kl.sendText(msg.to,Dmid)
            elif msg.text in ["TL:"]:
               if msg.from_ in admin: 
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                ki.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                kk.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                kc.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                kl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
               if msg.from_ in admin: 
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf+8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["LA rename "]:
               if msg.from_ in admin: 
                string = msg.text.replace("LA rename ","")
                if len(string.decode('utf+8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["WP rename "]:
               if msg.from_ in admin: 
                string = msg.text.replace("WP rename ","")
                if len(string.decode('utf+8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
               if msg.from_ in admin: 
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Blockinvite on","Guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Blockinvite On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Blockinvite On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Blockinvite off","Guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Blockinvite Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Blockinvite Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Blockcancel on","Cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Blockcancel On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Blockcancel On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Blockcancel off","Cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Blockcancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Blockcancel Off")
                    else:
                        cl.sendText(msg.to,"done")                        
            elif msg.text in ["Protect On","Protect on"]:
              if msg.from_ in admin:
                if wait["protection"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Kicker On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protection"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Kicker On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect Off","Protect off"]:
              if msg.from_ in admin:
                if wait["protection"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Kicker Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protection"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Kicker Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Autolike on","Auto like on"]:
              if msg.from_ in admin:
                if wait["autolike"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autolike"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Autolike off","Auto like off"]:
              if msg.from_ in admin:
                if wait["autolike"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autolike"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Off")
                    else:
                        cl.sendText(msg.to,"done")                        
            elif msg.text in ["Welcome On","Welcome on"]:
              if msg.from_ in admin:
                if wait["welcome"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ucapan Welcome On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["welcome"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ucapan Welcome On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Welcome Off","Welcome off"]:
              if msg.from_ in admin:
                if wait["welcome"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ucapan Welcome Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["welcome"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ucapan Welcome Off")
                    else:
                        cl.sendText(msg.to,"done")                        
            elif msg.text in ["Protectjoin on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Join On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Join On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protectjoin off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Join Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Join Off")
                    else:
                        cl.sendText(msg.to,"done")                        
            elif msg.text in ["Qr on","Protect qr on","Protectqr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","Protect qr off","Protectqr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","K on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","K off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
               if msg.from_ in admin: 
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
               if msg.from_ in admin: 
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
               if msg.from_ in admin: 
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
               if msg.from_ in admin: 
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
               if msg.from_ in admin: 
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
               if msg.from_ in admin: 
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
               if msg.from_ in admin: 
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Setting"]:
               if msg.from_ in admin: 
                md = ""
                if wait["Protectcancel"] == True: md+=" ➷Protect Cancel : ✔\n"
                else: md+=" ➷Protect Cancel : ✘\n"
                if wait["Protectjoin"] == True: md+=" ➷Protect Join : ✔\n"
                else: md+=" ➷Protect Join : ✘\n"
                if wait["protection"] == True: md+=" ➷Protect Kick : ✔\n"
                else: md+=" ➷Protect Kick : ✘\n"
                if wait["ProtectQR"] == True: md+=" ➷Protect Qr      : ✔\n"
                else: md+=" ➷Protect Qr   : ✘\n"
                if wait["Protectguest"] == True: md+=" ➷Block Invite : ✔\n"
                else: md+=" ➷Block Invite : ✘\n"
                if wait["contact"] == True: md+=" ➷Contact    : ✔\n"
                else: md+=" ➷Contact    : ✘\n"
                if wait["autoJoin"] == True: md+=" ➷Auto join : ✔\n"
                else: md +=" ➷Auto join : ✘\n"
                if wait["autoCancel"]["on"] == True:md+=" ➷Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " ➷Group cancel : ✘\n"
                if wait["leaveRoom"] == True: md+=" ➷Auto leave    : ✔\n"
                else: md+=" ➷Auto leave : ✘\n"
                if wait["timeline"] == True: md+=" ➷Share   : ✔\n"
                else:md+=" ➷Share   : ✘\n"
                if wait["autoAdd"] == True: md+=" ➷Auto add : ✔\n"
                else:md+=" ➷Auto add : ✘\n"
                if wait["commentOn"] == True: md+=" ➷Comment : ✔\n"
                else:md+=" ➷Comment : ✘\n"
                if wait["welcome"] == True: md+=" ➷Welcome : ✔\n"
                else:md+=" ➷Welcome : ✘\n"
                if wait["autolike"] == True: md+=" ➷Auto Like : ✔\n"
                else:md+=" ➷Auto Like : ✘\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall","Cancel all"]:
               if msg.from_ in admin: 
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
               if msg.from_ in admin: 
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
               if msg.from_ in admin: 
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
               if msg.from_ in admin: 
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
               if msg.from_ in admin: 
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
               if msg.from_ in admin: 
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["LA gurl"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["WP gurl"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Natsu gurl"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
               if msg.from_ in admin: 
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
               if msg.from_ in admin: 
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
               if msg.from_ in admin: 
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
               if msg.from_ in admin: 
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Start-------------------#
         #-------------Fungsi Cek Tag Start---------------------#				
	    elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass

                    
	#-------------Fungsi Cek Tag Done---------------------#                    
         #-------------Fungsi BC-------------------#
                    
            elif "Group bc " in msg.text:
               if msg.from_ in admin: 
                 bctxt = msg.text.replace("Group bc ", "")
                 n = cl.getGroupIdsJoined()
                 for manusia in n:
                      cl.sendText(manusia, (bctxt))
                      nl.sendText(manusia, (bctxt))

            elif "Contact bc " in msg.text:
               if msg.from_ in admin: 
                 bctxt = msg.text.replace("Contact bc ", "")
                 t = cl.getAllContactIds()
                 for manusia in t:
                      cl.sendText(manusia, (bctxt))
                      ki.sendText(manusia, (bctxt))
                      kk.sendText(manusia, (bctxt))
                      kc.sendText(manusia, (bctxt))
                      kl.sendText(manusia, (bctxt))
                      kj.sendText(manusia, (bctxt))
                      kh.sendText(manusia, (bctxt))
                      ka.sendText(manusia, (bctxt))
                      kz.sendText(manusia, (bctxt))
                      ks.sendText(manusia, (bctxt))
                      kb.sendText(manusia, (bctxt))
                      kw.sendText(manusia, (bctxt))
                      nl.sendText(manusia, (bctxt))

            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				kl.sendText(msg.to,(bctxt))
				kj.sendText(msg.to,(bctxt))
				kh.sendText(msg.to,(bctxt))
				ka.sendText(msg.to,(bctxt))
				kz.sendText(msg.to,(bctxt))
				ks.sendText(msg.to,(bctxt))
				kb.sendText(msg.to,(bctxt))
				kw.sendText(msg.to,(bctxt))
				nl.sendText(msg.to,(bctxt))
                    
         #-------------Fungsi BC Finish-------------------#

         #-------------Fungsi List group Start---------------------#                      

            elif msg.text in ["List group","List gc","List groupGc list"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[✞]%s\n" % (cl.getGroup(i).name   + " : " + str (len (cl.getGroup(i).members)))
                cl.sendText(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))

            elif msg.text in ["/ListIDGroup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n"
                            except:
                                h += "Error!"
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "|[Total Groups]| : " + total)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n"
                            except:
                                j += "Error!"
                                break
                        else:
                            break
                    if ginv is not None:
                        random.choice(KIL).sendText(msg.to,j + "|[Total Groups Invited]| : " + totals)
                    else:
                        random.choice(KIL).sendText(msg.to,"Tidak ada grup tertunda saat ini")
                
         #-------------Fungsi List Group Done---------------------#
         #-------------Fungsi Spam Pc Start---------------------#
            elif "Spam: " in msg.text:
                if msg.from_ in admin:
                    cond = msg.text.split(" ")
                    target = int(cond[1])
                    text = msg.text.replace("Spam: " + str(target) + "\nMessage: ","")
                    try:
                        ki.findAndAddContactsByMid(target)
                        ki.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                        ki.sendText(msg.to,"Berhasil mengirim pesan")
                    except:
                        ki.sendText(msg.to,"Gagal mengirim pesan, mungkin midnya salah")
         #-------------Fungsi Spam Pc Done---------------------#

             #----------------------------------------Fungsi Invite White Contact-------------------------------------------------#                         

            elif msg.text in ["Undang"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 random.choice(KIL).sendText(msg.to,"send contact 😉")                        
                if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 random.choice(KIL).sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 random.choice(KIL).sendText(msg.to,"Sorry, " + _name + " Kena Blacklist")
                                 random.choice(KIL).sendText(msg.to,"Suruh Admin Unban !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     kl.findAndAddContactsByMid(target)
                                     kl.inviteIntoGroup(msg.to,[target])
                                     random.choice(KIL).sendText(msg.to,"Saya Mengundangmu: \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         try:
                                             kw.findAndAddContactsByMid(invite)
                                             kw.inviteIntoGroup(op.param1,[invite])
                                             wait["winvite"] = False
                                             kw.sendText(msg.to,"Saya Mengundangmu���: \n➡" + _name)
                                             break
                                         except:
                                            try:
                                                 ka.findAndAddContactsByMid(invite)
                                                 ka.inviteIntoGroup(op.param1,[invite])
                                                 wait["winvite"] = False
                                                 ka.sendText(msg.to,"Saya Mengundangmu\n➡" + _name)
                                                 break
                                            except:
                                                 cl.sendText(msg.to,"Negative, Error detected")
                                                 wait["winvite"] = False
                                                 break
             #----------------------------------------Fungsi Invite White Contact-------------------------------------------------#  
                        
         #-------------Fungsi Spam Start---------------------#                      

            elif "Spam " in msg.text:
            	if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                  #Keke cantik ❤
                   if txt[1] == "on":
                        if jmlh <= 1000:
                             for x in range(jmlh):
                                   random.choice(KIL).sendText(msg.to, teks)
                        else:
                               random.choice(KIL).sendText(msg.to, "Limit Goblog! ")
                   elif txt[1] == "off":
                         if jmlh <= 1000000:
                               random.choice(KIL).sendText(msg.to, tulisan)
                         else:
                               random.choice(KIL).sendText(msg.to, "Limit Goblog! ")

            elif "Spamm " in msg.text:
            	if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spamm "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                  #Keke cantik ❤
                   if txt[1] == "out":
                        if jmlh <= 1000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                              cl.sendText(msg.to, "Limit Goblog! ")
                   elif txt[1] == "in":
                         if jmlh <= 1000000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Limit Goblog! ")



                               
         #-------------Fungsi Spam Done---------------------#
         #-------------Fungsi Ban Tag Start---------------------#

            elif ("Bl " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      random.choice(KIL).sendText(msg.to,"Succes Banned")
                   except:
                      pass

         #-------------Fungsi Ban Tag Done---------------------#

         #-------------Fungsi Kick Leave Start---------------------#                    
            elif "Anu " in msg.text:
                  if msg.from_ in admin:
                       ulti0 = msg.text.replace("Anu ","")
                       ulti1 = ulti0.lstrip()
                       ulti2 = ulti1.replace("@","")
                       ulti3 = ulti2.rstrip()
                       _name = ulti3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       nl.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.1)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           random.choice(KIL).sendText(msg.to,"User Tidak Ditemukan")
                           pass
                       else:
                           for target in targets:
                                try:
                                    nl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:                                                                        
                                    nl.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    ki.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    kl.updateGroup(gs)


         #-------------Fungsi Kick Leave Start---------------------#                 
				
         #-------------Fungsi Unban Tag Start---------------------#
            elif ("Wl " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait["blacklist"][target]
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      random.choice(KIL).sendText(msg.to,"Akun Telah Di Unban")
                   except:
                      pass
	#-------------Fungsi Unban Tag Done---------------------#

            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                random.choice(KIL).sendText(msg.to,"Clear All Ban Done")

         #-------------Fungsi Kick Tag Start---------------------#

            elif ("Kill " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KIL).kickoutFromGroup(msg.to,[target])
                   except:
                      pass

         #-------------Fungsi Kick Tag Done---------------------#
                               
         #-------------Fungsi Add Admin Start---------------------# 


            elif "Admin add @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = random.choice(KIL).getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KIL).sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                random.choice(KIL).sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    random.choice(KIL).sendText(msg.to,"Command denied.")
                    random.choice(KIL).sendText(msg.to,"Admin permission required.")

            elif "Admin remove @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = random.choice(KIL).getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KIL).sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                random.choice(KIL).sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    random.choice(KIL).sendText(msg.to,"Command denied.")
                    random.choice(KIL).sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Adminlist","Admin list"]:
                if admin == []:
                    random.choice(KIL).sendText(msg.to,"The stafflist is empty")
                else:
                    random.choice(KIL).sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    random.choice(KIL).sendText(msg.to,mc)
                    print "[Command]Stafflist executed"

         #-------------Fungsi Add Admin Done---------------------#

         #-------------Fungsi Add Staff Start---------------------# 


            elif "Staff add @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = random.choice(KIL).getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KIL).sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                Bots.append(target)
                                random.choice(KAC).sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    random.choice(KIL).sendText(msg.to,"Command denied.")
                    random.choice(KIL).sendText(msg.to,"Admin permission required.")

            elif "Staff remove @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = random.choice(KIL).getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KIL).sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                Bots.remove(target)
                                random.choice(KIL).sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    random.choice(KIL).sendText(msg.to,"Command denied.")
                    random.choice(KIL).sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","Staff list"]:
                if admin == []:
                    random.choice(KIL).sendText(msg.to,"The stafflist is empty")
                else:
                    random.choice(KIL).sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in Bots:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    random.choice(KIL).sendText(msg.to,mc)
                    print "[Command]Stafflist executed"

         #-------------Fungsi Add Staff Done---------------------#                    

            elif "/CancelInvited: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("/CancelInvited: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")

            elif "/AcceptInvitation: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/AcceptInvitation: ","")
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")

            elif msg.text in ["/AcceptAllInvitation"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")                    

         #-------------Fungsi COPY Name Start---------------------#                      
            elif "Name @" in msg.text:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    print "[Name]"
                    _name = msg.text.replace("Name @","")
                    _nametarget = _name.rstrip('  ')                    
                    gs = cl.getGroup(msg.to)                    
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:                        
                        cl.sendText(msg.to,"Tidak Ada Target ")                        
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target).statusMessage                                
                                contact2 = cl.getContact(target).displayName
                                copy = cl.getProfile()
                                copy.statusMessage = contact                                
                                copy.displayName = contact2
                                cl.updateProfile(copy)
                                sendText(msg.to, "Copy Name Done")
                            except:                                
                                pass                                                         
                                
         #-------------Fungsi COPY Name Done---------------------#
         #-------------Fungsi COPY Start---------------------#

            elif msg.text in ["Kembali"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Kembali Seperti Semula")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                            
            elif "Copy @" in msg.text:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    print "[Copy]"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip('  ')                    
                    gs = cl.getGroup(msg.to)                    
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:                        
                        cl.sendText(msg.to,"Tidak Ada Target ")                        
                    else:
                        for target in targets:
                            try:
                                cl.CloneContactProfile(target)
                                cl.sendText(msg.to, "Copy Done")
                            except Exception as e:
                                print e
         #-------------Fungsi COPY Done---------------------#
                            
            elif msg.text in ["Creator"]:              
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ubce1a713f0cd01fa3b402ebd3e72ecb1'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"My Creator")
                random.choice(KIL).sendText(msg.to,"My Creator")
            elif msg.text in ["Gcreator:inv"]:
             if msg.from_ in admin:   
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass                                 
                      
         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
               if msg.from_ in admin: 
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update""Jam update""Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "Setp":
                    cl.sendText(msg.to, "Setpoint")                    
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"(%H:%M)")
                    wait2['ROM'][msg.to] = {}
                    print wait2
                
            elif msg.text == "Cek":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Setpoint Dulu Tolol 􀜁􀅔Har Har􏿿 「Setp」")
                    pass
                #-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Kuy join","All join","Ayo masuk","Join all"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kz.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kw.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)  
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text in ["Join 1"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)


            elif msg.text in ["Join 2"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kz.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kw.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)  
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)                        

                        

            elif msg.text in ["LA join"]:
              if msg.form_ in admin:
                  X = ki.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  ki.updateGroup(X)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["WP join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Ian join"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Natsu join"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Yatogami join"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)    
    #----------------------Fungsi Join Group Finish---------------#

    #----------------------Fungsi Steal Start-------------------------#

            elif "Steal: " in msg.text:
                if msg.from_ in admin:
                    salsa = msg.text.replace("Steal: ","")
                    Manis = cl.getContact(salsa)
                    contact = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)


                        
            elif "Stealpict " in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        msg.contentType = 0
                        steal0 = msg.text.replace("Stealpict ","")
                        steal1 = steal0.lstrip()
                        steal2 = steal1.replace("@","")
                        steal3 = steal2.rstrip()
                        _name = steal3
                        group = cl.getGroup(msg.to)
                        targets = []
                        for g in group.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"User yang di tag tidak valid")
                        else:
                            for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    try:
                                        cover = cl.channel.getCover(contact)
                                    except:
                                        cover = ""
                                    try:
                                        cl.sendText(msg.to,"Gambar Foto Profilenya")
                                        cl.sendImageWithURL(msg.to,image)
                                        if cover == "":
                                            cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                                        else:
                                            cl.sendText(msg.to,"Gambar Covernya")
                                            cl.sendImageWithURL(msg.to,cover)
                                    except Exception as error:
                                        cl.sendText(msg.to,(error))
                                        break
                                except:
                                    cl.sendText(msg.to,"Error!")
                                    break
                    else:
                        cl.sendText(msg.to,"Tidak bisa dilakukan di luar wilayah")



     #----------------------Fungsi Steal Done--------------------------#                 

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Bye all","Babay"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kl.leaveGroup(msg.to)
                        kj.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kz.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        kw.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 1"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kl.leaveGroup(msg.to)
                        kj.leaveGroup(msg.to)                        
                    except:
                        pass
            elif msg.text in ["Bye all","Babay"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:                        
                        kh.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kz.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        kw.leaveGroup(msg.to)
                    except:
                        pass                    
            elif msg.text in ["Bye LA"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye WP"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Natsu"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Yatogami"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Ian"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass                    
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tagall User Start---------------#
            elif msg.text in ["Mentionall"]:
                if msg.from_ in admin:
    			group = cl.getGroup(msg.to)
    			nama = [contact.mid for contact in group.members]
    			cb = ""
    			cb2 = ""
    			strt = int(0)
    			akh = int(0)
    			for md in nama:
        			akh = akh + int(5)
        			cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
        			strt = strt + int(6)
        			akh = akh + 1
        			cb2 += "@nrik\n"
    			cb = (cb[:int(len(cb)-1)])
    			msg.contentType = 0
    			msg.text = cb2
    			msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
    			try:
        			cl.sendMessage(msg)
    			except Exception as error:
        			print error

            elif msg.text in ["Tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]                                
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for o in range(400, len(nama)-1):
                        nm5 += [nama[o]]
                    mention(msg.to, nm5)
                cnt = Message()
                cnt.text = "Done:"+str(jml)
                cnt.to = msg.to
                cl.sendText(cnt)
        			

    #-------------Fungsi Tagall User Finish-------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Selamat tinggal")
                        kc.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,kl,kj,kh,ka,kz,ks,kb,kw]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                
            elif "Ratakan" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    ki.sendText(msg.to,"Grup Kontlo Ini Mah")
                    kk.sendText(msg.to,"Rata G Rata Yg Penting Play")
                    kc.sendText(msg.to,"TANGKIS GOBLOG")
                    cl.sendText(msg.to,"Fuck You All")
                    kl.sendText(msg.to,"KONTOL")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                        kc.sendText(msg.to,"Not found.")
                        cl.sendText(msg.to,"Not found.")
                        kl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[cl,ki,kk,kc,kl,kj,kh,ka,kz,ks,kb,kw]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
                                kk.sendText(msg.to,"Group cleanse")
                                kc.sendText(msg.to,"Group cleanse")
                                cl.sendText(msg.to,"Group cleanse")
                                kl.sendText(msg.to,"Group cleanse")
            
        #----------------Fungsi Kick User Target Start----------------------#
            elif "Bunuh " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Bunuh ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc,kl,kj,kh,ka,kz,ks,kb,kw]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Semoga Diterima Disisinya")                                    
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
               if msg.from_ in admin: 
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kw.sendText(msg.to,"Succes")
                                except:
                                    ki.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Ban @" in msg.text:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = random.choice(KIL).getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KIL).sendText(msg.to,"Tidak Ditemukan")                        
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KIL).sendText(msg.to,"Succes Bosq")                                
                            except:
                                random.choice(KIL).sendText(msg.to,"Error")                                
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = random.choice(KIL).getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KIL).sendText(msg.to,"Tidak Ditemukan.....")                        
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KIL).sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                random.choice(KIL).sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
               if msg.from_ in admin: 
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ka.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kz.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ks.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kb.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kw.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                
                
                
                
        #-------------Fungsi Spam Finish---------------------#
         
#-----------------------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				random.choice(KIL).sendText(msg.to,(bctxt))				
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","respon","Respon Dong","respon dong"]:
               if msg.from_ in admin: 
                cl.sendText(msg.to,"IaN 􀔃􀄆red check mark􏿿")
                ki.sendText(msg.to,"Tsuna 􀔃􀄆red check mark􏿿")
                kk.sendText(msg.to,"Laxus 􀔃􀄆red check mark􏿿")
                kc.sendText(msg.to,"Natsu 􀔃􀄆red check mark􏿿")
                kl.sendText(msg.to,"Yatogami 􀔃􀄆red check mark􏿿")
                kj.sendText(msg.to,"Sasuke 􀔃􀄆red check mark􏿿")
                kh.sendText(msg.to,"Itachi 􀔃􀄆red check mark􏿿")
                ka.sendText(msg.to,"Yahiko 􀔃􀄆red check mark􏿿")
                kz.sendText(msg.to,"Shirouo 􀔃􀄆red check mark􏿿")
                ks.sendText(msg.to,"Kaneki 􀔃􀄆red check mark􏿿")
                kb.sendText(msg.to,"Wolf Police 􀔃􀄆red check mark􏿿")
                kw.sendText(msg.to,"Lord Angel 􀔃􀄆red check mark􏿿")
      #-------------Fungsi Respon Finish---------------------#

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Utama Start---------------------#
            elif msg.text in ["Sp","Speed","speed"]:
               if msg.from_ in admin  and Bots: 
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
    
        #-------------Fungsi Speedbot Kedua Start---------------------# 
            elif msg.text in ["LA Sp","LA speed","Sp la"]:
               if msg.from_ in admin: 
                start = time.time()
                kw.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                kw.sendText(msg.to, "%sseconds" % (elapsed_time))
        #-------------Fungsi Speedbot Ketiga Start---------------------#
            elif msg.text in ["WP Sp","WP speed","Sp wp"]:
               if msg.from_ in admin: 
                start = time.time()
                kb.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                kb.sendText(msg.to, "%sseconds" % (elapsed_time))

         #-------------Fungsi Speedbot Keempat Start---------------------#
            elif msg.text in ["Yatogami Sp","Yatogami speed","Sp yatogami"]:
               if msg.from_ in admin: 
                start = time.time()
                kc.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                kl.sendText(msg.to, "%sseconds" % (elapsed_time))
        #-------------Fungsi Speedbot Kelima Start---------------------#
        #-------------Fungsi Speedbot Kelima Start---------------------#
            elif "GroupCreator" == msg.text:
                            try:
                                group = cl.getGroup(msg.to)
                                GS = group.creator.mid
                                M = Message()
                                M.to = msg.to
                                M.contentType = 13
                                M.contentMetadata = {'mid': GS}
                                random.choice(KIL).sendMessage(M)
                            except:
                                W = group.members[0].mid
                                M = Message()
                                M.to = msg.to
                                M.contentType = 13
                                M.contentMetadata = {'mid': W}
                                random.choice(KIL).sendMessage(M)
                                random.choice(KIL).sendText(msg.to,"old user")
        #-------------Fungsi Speedbot Semua Start---------------------#
            elif msg.text in ["All sp","All speed","Speed all","Sp all"]:
               if msg.from_ in admin: 
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s seconds" % (elapsed_time))
                ki.sendText(msg.to, "Progress...")
                ki.sendText(msg.to, "%s seconds" % (elapsed_time))
                kk.sendText(msg.to, "Otw...")
                kk.sendText(msg.to, "%s seconds" % (elapsed_time))
                kc.sendText(msg.to, "Menunggu...")
                kc.sendText(msg.to, "%s seconds" % (elapsed_time))
                kl.sendText(msg.to, "Sabar...")
                kl.sendText(msg.to, "%s seconds" % (elapsed_time))
                kj.sendText(msg.to, "Waiting...")
                kj.sendText(msg.to, "%s seconds" % (elapsed_time))
                kh.sendText(msg.to, "Waiting...")
                kh.sendText(msg.to, "%s seconds" % (elapsed_time))
                ka.sendText(msg.to, "Waiting...")
                ka.sendText(msg.to, "%s seconds" % (elapsed_time))
                kz.sendText(msg.to, "Waiting...")
                kz.sendText(msg.to, "%s seconds" % (elapsed_time))
                ks.sendText(msg.to, "Waiting...")
                ks.sendText(msg.to, "%s seconds" % (elapsed_time))
                kb.sendText(msg.to, "Waiting...")
                kb.sendText(msg.to, "%s seconds" % (elapsed_time))
                kw.sendText(msg.to, "Waiting...")
                kw.sendText(msg.to, "%s seconds" % (elapsed_time))
                
        #-------------Fungsi Speedbot Finish---------------------#
      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
               if msg.from_ in admin: 
                wait["wblacklist"] = True
                random.choice(KIL).sendText(msg.to,"Kirim Kontak")                
            elif msg.text in ["Unban"]:
               if msg.from_ in admin: 
                wait["dblacklist"] = True
                random.choice(KIL).sendText(msg.to,"Kirim Kontak")                
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist","Listban"]:
               if msg.from_ in admin: 
                if wait["blacklist"] == {}:
                    random.choice(KIL).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KIL).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    random.choice(KIL).sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KIL).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KIL).sendText(msg.to,"Disini Tidak Ada Blacklist")                        
                        return
                    for jj in matched_list:
                        random.choice(KIL).kickoutFromGroup(msg.to,[jj])                        
                    random.choice(KIL).sendText(msg.to,"Fuck You Blacklist")                    
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    random.choice(KIL).sendText(msg.to,"I pretended to cancel and canceled.")
            elif "Random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("Random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")                               
                
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"] + nowT
                kc.updateProfile(profile4)
            time.sleep(600)                
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
