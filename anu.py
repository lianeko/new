# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

#cl = LINETCR.LINE()
#cl.login(qr=True)
#cl.loginResult()

#ki = LINETCR.LINE()
#ki.login(qr=True)
#ki.loginResult()

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

#kc = LINETCR.LINE()
#kc.login(qr=True)
#kc.loginResult()

#kl = LINETCR.LINE()
#kl.login(qr=True)
#kl.loginResult()

cl = LINETCR.LINE()
cl.login(token="ElPLI2yzbnYs4gdFvaK4.6OowBXq+Jy0nf7bEbCA0ba.DKJ4J2RaBherKWbyDDKOiYXfSiu4tyDm2K0WB5618AQ=")

ki = LINETCR.LINE()
ki.login(token="ElmuDTcKWibr8V2NT6d0.PQVf82HpryeddPW9tbCmma.HvGT+wlEi4lwzkq5CXkHOZaiRLh6sMKFuWLvgkumsgU=")

kk = LINETCR.LINE()
kk.login(token="El9bdbAtDPCqtFMFvJK4.Z/KYWQ4jucOEPlEi6sn7ra.qNcn1Pf/L8gIfap4oGfHS8dvYjsH8Mpy/IXGq9lP4a4=")

kc = LINETCR.LINE()
kc.login(token="ElwMh2DWktojs1sNzfw6.fZ6Oit60RnHeCLKcjobFzG.oqbzFldcWLe/EO4nWkH3oTt+txsqDqFxVj4BzYycCro=")

kl = LINETCR.LINE()
kl.login(token="ElDKAF8uQmpLW6tkzC0e.0oz4ZwAHo3Bvivjx8lNH3G.FGrEztgfBHMktEZlqt622+8guARvCUtQkG/PhW1CdlA=")

cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ✞ I҉a҉N ҉B҉O҉T҉ ME҉N҉U҉ ✞

􀔃􀅕red arrow right􏿿 Command Public
✞[Ian?] Cek Akun Bot
✞[Update] Update jam Bot
✞[Gid] Cek Id Group
✞[Ginfo] Group Info
✞[All mid] Cek All mid Bot
✞[IaN/LA/WP/XxX] Cek Mid Bot
✞[Respon] Cek Respon Bot
✞[Speed/Sp Nama Bot] Cek Kecepatan Bot
✞[Up] Fungsi Spam Chat
✞[Banlist/Listban] Cek List Akun Banned
✞[Gn namagroup] Ganti Nama Group
✞[Cancel] Cancel User Masuk Group
✞[Mentionall]      Mention Semua User
✞[Set View] Cek Privasi Group
✞[Open Url/Ourl]  Membuka Url Group
✞[Close Url/Curl] Menutup Url Group

􀔃􀅕red arrow right􏿿 Command Private
✞[SetGroup] Menggatur Privasi Grup
✞[Kill ban] Kick Blacklist
✞[Ban @] Bann Target
✞[Unban @]  Unbann Target
✞[Kill @] Kick Target Bann
✞[Nk @]   Kick Target User
✞[All join] Invite Semua Bot
✞[_namabot join] Invite Bot
✞[Bye _namabot]  Leave Bot

✞My Creator Http://line.me/ti/p/~lianekof
"""

Setgroup =""" ✞Privasi Menu  􀔃􀄆red check mark􏿿✞

✞[Protect QR -- Qr on / off]
✞[Mid Via Contact -- Contact On / Off]
✞[Reject Invite -- Guest On / Off]
"""
KAC=[cl,ki,kk,kc,kl,"ubce1a713f0cd01fa3b402ebd3e72ecb1"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kl.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["ubce1a713f0cd01fa3b402ebd3e72ecb1","uea83966f143f8d8d0d17b05e05c6b404","ua6abc5f3684f4581030e9c3d4c170c30","u173ea8213eb4acd84472590224e05f66"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add me,My Creator Http://line.me/ti/p/~lianekof",
    "lang":"JP",
    "comment":"Thanks for add me,My Creator Http://line.me/ti/p/~lianekof",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"⠀‮  ™NaI",
    "cName2":"Lord Angel",
    "cName3":"Wolf Police",
    "cName4":"x̶x̶x̶",
    "cName5":"Yatogami",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    try:
        cl.sendText(op.param1, "Welcome Sayang\nJangan Nakal Ya Kak " + client.getContact(op.param2).displayName)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return    

def NOTIFIED_READ_MESSAGE(op):
    try:
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

def autolike():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked']:
            try:
                cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                cl.comment(hasil['result']['posts'][zx]['postInfo']['liked'],hasil['result']['posts'][zx]['postingInfo']['postId'],"Auto Like By IaN™")
                ki.comment(hasil['result']['posts'][zx]['postInfo']['liked'],hasil['result']['posts'][zx]['postingInfo']['postId'],"My Creator Http://line.me/ti/p/~lianekof")
                print "Like"
            except:
                pass
        else:
            print "Already Liked"                  
    time.sleep(500)                               
                          


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
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    ki.sendText(op.param1,str(wait["message"]))
                    kc.sendText(op.param1,str(wait["message"]))
                    kk.sendText(op.param1,str(wait["message"]))
                    kl.sendText(op.param1,str(wait["message"]))

        #------Open QR Kick start------#
        if op.type == 10:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   klist=[cl,ki,kk,kc,kl]
                   kicker=random.choice(klist)
                   kicker.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

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
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])

        if op.type == 19:
           if op.param2 not in Bots:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
           if op.param2 not in Bots:
              cl.kickoutFromGroup(op.param1,[op.param2])
              cl.inviteIntoGroup(op.param1,admin) 
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param2],admin)
              kl.kickoutFromGroup(op.param1,[op.param2])
              kl.inviteIntoGroup(op.param1,admin)
           else:
               pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    klk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
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
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message

        #------Cancel User Kick start------#
        if op.type == 32:
            if op.param2 not in Bots:
               cl.kickoutFromGroup(op.param1,[op.param2])
               ki.kickoutFromGroup(op.param1,[op.param2])
               kk.kickoutFromGroup(op.param1,[op.param2])
               kc.kickoutFromGroup(op.param1,[op.param2])
               kl.kickoutFromGroup(op.param1,[op.param2])
        #-----Cancel User Kick Finish------#

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done Hapus")
                        ki.sendText(msg.to,"Done Hapus")
                        kk.sendText(msg.to,"Done Hapus")
                        kc.sendText(msg.to,"Done Hapus")
                        kl.sendText(msg.to,"Done Hapus")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak Ada Blacklist")
                        ki.sendText(msg.to,"Tidak Ada Blacklist")
                        kk.sendText(msg.to,"Tidak Ada Blacklist")
                        kc.sendText(msg.to,"Tidak Ada Blacklist")
                        kl.sendText(msg.to,"Tidak Ada Blacklist")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Sudah Terbanned")
                        ki.sendText(msg.to,"Sudah Terbanned")
                        kk.sendText(msg.to,"Sudah Terbanned")
                        kc.sendText(msg.to,"Sudah Terbanned")
                        kl.sendText(msg.to,"Sudah Terbanned")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                        ki.sendText(msg.to,"Done")
                        kk.sendText(msg.to,"Done")
                        kc.sendText(msg.to,"Done")
                        kl.sendText(msg.to,"Done")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done Hapus")
                        ki.sendText(msg.to,"Done Hapus")
                        kk.sendText(msg.to,"Done Hapus")
                        kc.sendText(msg.to,"Done Hapus")
                        kl.sendText(msg.to,"Done Hapus")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Tidak Ada Blacklist")
                        ki.sendText(msg.to,"Tidak Ada Blacklist")
                        kk.sendText(msg.to,"Tidak Ada Blacklist")
                        kc.sendText(msg.to,"Tidak Ada Blacklist")
                        kl.sendText(msg.to,"Tidak Ada Blacklist")
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
            elif msg.text in ["SetGroup"]:
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
            elif ("WP gn " in msg.text):
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("WP gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("XxX gn " in msg.text):
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("XxX gn ","")
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
            elif "XxX kick " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("XxX kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
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
            elif "XxX invite " in msg.text:
               if msg.from_ in admin: 
                midd = msg.text.replace("XxX invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Bot Ian"]:
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
                kc.sendMessage(msg)                
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
            elif msg.text in ["XxX"]:
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
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","XxX gift"]:
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
            elif msg.text in ["WP cancel","LA cancel"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"Tidak Ada yang Bisa Dicancel")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
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
                        ki.sendText(msg.to,"Done IaN")
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
                        kk.sendText(msg.to,"Done IaN")
                    else:
                        kk.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["XxX ourl","XxX link on"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done IaN")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
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
                        ki.sendText(msg.to,"Done IaN")
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
                        kk.sendText(msg.to,"Done IaN")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["XxX curl","XxX link off"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done IaN")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
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
            elif "XxX" == msg.text:
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
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                kl.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
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
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["LA rename "]:
               if msg.from_ in admin: 
                string = msg.text.replace("LA rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["WP rename "]:
               if msg.from_ in admin: 
                string = msg.text.replace("WP rename ","")
                if len(string.decode('utf-8')) <= 20:
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
            elif msg.text in ["Guest On","Guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","Guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
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
            elif msg.text in ["Qr off","qr off"]:
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
            elif msg.text in ["Contact On","Contact on","K off"]:
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
            elif msg.text in ["Contact Off","Contact off","contact off"]:
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
            elif msg.text in ["Set"]:
               if msg.from_ in admin: 
                md = ""
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Protect Qr      : on\n"
                else: md+=" Protect Qr   : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
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
            elif msg.text in ["XxX gurl"]:
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
                    kc.sendText(msg.to,"Bot 4 jam on")
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
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Finish-------------------#           
         
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

            elif msg.text == "Sett":
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Setpoint")                    
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2
                
            elif msg.text == "Cek":
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendMessage(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
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
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)                        
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
                  
            elif msg.text in ["XxX join"]:
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
            elif msg.text in ["Bye XxX"]:
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
                            klist=[ki,kk,kc,kl]
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
                                klist=[ki,kk,kc,cl,kl]
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
                                    klist=[cl,ki,kk,kc,kl]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Semoga Diterima Disisinya")
                                    kc.sendText(msg.to,"Hehehe")
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
               if msg.from_ in admin: 
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
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
                                    k3.sendText(msg.to,"Succes Cv")
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
                    gs = kc.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found LA")
                        kk.sendText(msg.to,"Not found WP")
                        kc.sendText(msg.to,"Not found XxX")
                        cl.sendText(msg.to,"Not found IaN")
                        kl.sendText(msg.to,"Not found Yatogami")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes IaN")
                                ki.sendText(msg.to,"Succes LA")
                                kk.sendText(msg.to,"Succes WP")
                                kc.sendText(msg.to,"Succes XxX")
                                kl.sendText(msg.to,"Succes Yatogami")
                            except:
                                ki.sendText(msg.to,"Error")
                                kk.sendText(msg.to,"Error")
                                kc.sendText(msg.to,"Error")
                                cl.sendText(msg.to,"Error")
                                kl.sendText(msg.to,"Error")
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
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
               if msg.from_ in admin: 
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀔃􀆶squared up!􏿿")
                
                
                
        #-------------Fungsi Spam Finish---------------------#
#-----------------------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				kl.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Ian say hi"]:
               if msg.from_ in admin: 
                ki.sendText(msg.to,"Hi Om 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi Tante 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi Semuanya 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Ian say Alo Fans"]:
               if msg.from_ in admin: 
                ki.sendText(msg.to,"Alo Fans 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Alo Fans 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Alo Fans 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Ian say UP MUMBUL"]:
               if msg.from_ in admin: 
                ki.sendText(msg.to,"UP MUMBUL 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"UP MUMBUL 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"UP MUMBUL 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Ian say bobo ah","Bobo dulu ah"]:
               if msg.from_ in admin: 
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Ian say ians pekok"]:
               if msg.from_ in admin: 
                ki.sendText(msg.to,"Ians pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Ians pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Ians pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di IaN Family Room")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","respon","Respon Dong","respon dong"]:
               if msg.from_ in admin: 
                cl.sendText(msg.to,"IaN Hadir")
                ki.sendText(msg.to,"Lord Angel Hadir")
                kk.sendText(msg.to,"Wolf Police Hadir")
                kc.sendText(msg.to,"XxX Hadir")
                kl.sendText(msg.to,"Yatogami Hadir")
      #-------------Fungsi Respon Finish---------------------#

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Utama Start---------------------#
            elif msg.text in ["Sp","Speed","speed"]:
               if msg.from_ in admin: 
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
    
        #-------------Fungsi Speedbot Kedua Start---------------------# 
            elif msg.text in ["LA Sp","LA speed","Sp la"]:
               if msg.from_ in admin: 
                start = time.time()
                ki.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
        #-------------Fungsi Speedbot Ketiga Start---------------------#
            elif msg.text in ["WP Sp","WP speed","Sp wp"]:
               if msg.from_ in admin: 
                start = time.time()
                kk.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                kk.sendText(msg.to, "%sseconds" % (elapsed_time))

         #-------------Fungsi Speedbot Keempat Start---------------------#
            elif msg.text in ["Yatogami Sp","Yatogami speed","Sp yatogami"]:
               if msg.from_ in admin: 
                start = time.time()
                kc.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                kl.sendText(msg.to, "%sseconds" % (elapsed_time))
        #-------------Fungsi Speedbot Kelima Start---------------------#

                
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
                
        #-------------Fungsi Speedbot Finish---------------------#
      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
               if msg.from_ in admin: 
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim Kontak")
                ki.sendText(msg.to,"Kirim Kontak")
                kk.sendText(msg.to,"Kirim Kontak")
                kc.sendText(msg.to,"Kirim Kontak")
                kl.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Unban"]:
               if msg.from_ in admin: 
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim Kontak")
                ki.sendText(msg.to,"Kirim Kontak")
                kk.sendText(msg.to,"Kirim Kontak")
                kc.sendText(msg.to,"Kirim Kontak")
                kl.sendText(msg.to,"Kirim Kontak")
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist","Listban"]:
               if msg.from_ in admin: 
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    ki.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
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
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Disini Tidak Ada Blacklist")
                        ki.sendText(msg.to,"Disini Tidak Ada Blacklist")
                        kk.sendText(msg.to,"Disini Tidak Ada Blacklist")
                        kc.sendText(msg.to,"Disini Tidak Ada Blacklist")
                        kl.sendText(msg.to,"Disini Tidak Ada Blacklist")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                        kl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Fuck You Blacklist")
                    ki.sendText(msg.to,"Fuck You Blacklist")
                    kk.sendText(msg.to,"Fuck You Blacklist")
                    kc.sendText(msg.to,"Fuck You Blacklist")
                    kl.sendText(msg.to,"Fuck You Blacklist")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
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
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile5 = kl.getProfile()
                profile5.displayName = wait["cName5"]
                kl.updateProfile(profile5)                
                
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
