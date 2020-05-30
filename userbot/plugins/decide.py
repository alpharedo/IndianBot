""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd("join"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd("pay"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Payment info:**/n/nPaytm wallet: 9426228693/nPaytm Upi: 9426228693@paytm/n/nSend Screenshot after Payment.🤘"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd("netflix"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "🤘 NETFLIX ON SALE 🤘\n\n✌️ ACCOUNT PRIVATE\n✌️ PASSWORD CHANGEABLE\n✌️4 SCREEN | UHD QUALITY\n✌️30 DAYS VALIDITY + MIGHT GET AUTORENEW AND WORK LONGER.\n✌️21 DAYS GURANTEED WITH REPLACEMENT OR REFUND\n✌️PASSWORD CAN BE RECOVER IF YOU FORGET__\n\nAVAILABLE IN STOCK\n\nPRICE ₹150/-\n\n📩IB ME TO BUY\n\nFor Proofs Dm Me\n\nDISCOUNT AVAILABLE FOR RESELLERS AND BULK BUYERS\n\nESCROW ACCEPTED  WITH TRUSTED ONES✔️"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd("reseller"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "NETFLIX ACCOUNT AVAILABE\n\n➡️ PRIVATE ACCOUNT\n➡️ 4+1 SCREEN\n➡️ PREMIUM PLAN\n➡️ ULTRA HD\n➡️ WORKING IN ALL DEVICE\n➡️ PASSWORD CHANGEABLE\n➡️ 25 DAYS GUARANTEE\n➡️ ESCROW ACCEPTED\n\n📱MADE ACCOUNTS📱\n\nPRICE IN BULK-\n\nRs. 100 (10 Accounts for Rs.1000).\nRs. 115 (5 Accounts for Rs. 575).\nRs. 130 (1 Account for Rs. 130).\n\nOnly Prepaid Orders will be accepted.\n\nDM TO BUY\n\nFOR BULK BUYERS\n\nESCROW ACCEPTED"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
