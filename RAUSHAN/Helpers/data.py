from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 
from config import Config

PM_TEXT = """
**✦ » ʜᴇʏ {},**
**✦ » ɪ ᴀᴍ {} - ᴀ ʙᴏᴛ ғᴏʀ ᴛɢ ɪᴅ ᴅᴇᴛᴀɪʟs ᴠɪᴀ sᴛʀɪɴɢ sᴇssɪᴏɴ.**

**✦ » sᴜᴘᴘᴏʀᴛs ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴs. ᴄʟɪᴄᴋ ᴏɴ ʜᴀᴄᴋ ᴛᴏ sᴇᴇ ғᴇᴀᴛᴜʀᴇs.**

**✦ » ᴘᴏᴡᴇʀᴇᴅ ʙʏ » [⎯᪵፝֟፝֟⎯꯭𓆩꯭ ꯭𝐀 ꯭ʟ ꯭ᴘ ꯭ʜ꯭ ᴧ꯭⎯꯭꯭‌꯭🥂꯭༎꯭ 𓆪](http://t.me/TheSigmaCoder)**
"""

HACK_TEXT = """
**𝗔 :~** [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴏᴡɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs]

**𝗕 :~** [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴜsʀɴᴀᴍᴇ... ᴇᴛᴄ]

**𝗖 :~** [ʙᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ sᴛʀɪɴɢsᴇssɪᴏɴ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛʜᴇʀᴇ}]

**𝗗 :~** [ᴋɴᴏᴡ ᴜsᴇʀ ʟᴀsᴛ ᴏᴛᴘ {𝟷sᴛ ᴜsᴇ **ᴏᴘᴛɪᴏɴ ʙ** ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ ᴀᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜsᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}]

**𝗘 :~** [ᴊᴏɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠɪᴀ sᴛʀɪɴɢsᴇssɪᴏɴ]

**𝗙 :~** [ʟᴇᴀᴠᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠɪᴀ sᴛʀɪɴɢsᴇssɪᴏɴ]

**𝗚 :~** [ᴅᴇʟᴇᴛᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

**𝗛 :~** [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴛᴡᴏ sᴛᴇᴘ ɪs ᴇɴᴇᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ]

**𝗜 :~** [ᴛᴇʀᴍɪɴᴀᴛᴇ ᴀʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs ᴇxᴄᴇᴘᴛ ᴜᴏᴜʀ sᴛʀɪɴɢsᴇssɪᴏɴ]

**𝗝 :~** [ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ]

**𝗞 :~** [ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

**𝗟 :~** [ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]
"""

info = """
❥︎ ɴᴀᴍᴇ : {}
❥︎ ɪᴅ : {}
❥︎ ᴘʜᴏɴᴇ ɴᴏ : +{}
❥︎ ᴜsᴇʀɴᴀᴍᴇ : @{}
"""

PM_BUTTON = IKM([
    [IKB("•─╼⃝𖠁 ʜᴀᴄᴋ 𖠁⃝╾─•", callback_data="hack_btn")],
    [
        IKB("˹ᴏᴡɴᴇʀ˼", user_id=Config.OWNER_ID),
        IKB("˹ᴜᴘᴅᴀᴛᴇs˼", url="https://t.me/purvi_bots"),
    ],
    [
        IKB("˹ᴍᴜsɪᴄ ʙᴏᴛ˼", url="https://t.me/SonaliMusicBot"),
        IKB("˹ʙᴏᴛ sᴏᴜʀᴄᴇ˼", url="https://github.com/TEAMPURVI/STRING_HACK"),
    ],
    [IKB("˹ᴀʟʟ-ʙᴏᴛs˼", url="https://t.me/PurviBots")]
])



HACK_MODS = IKM(
    [
        [
            IKB("𝗔", callback_data="A"),
            IKB("𝗕", callback_data="B"),
            IKB("𝗖", callback_data="C"),
            IKB("𝗗", callback_data="D"),
        ],
        [
            IKB("𝗘", callback_data="E"),
            IKB("𝗙", callback_data="F"),
            IKB("𝗚", callback_data="G"),
            IKB("𝗛", callback_data="H"),
        ],
        [
            IKB("𝗜", callback_data="I"),
            IKB("𝗝", callback_data="J"),
            IKB("𝗞", callback_data="K"),
            IKB("𝗟", callback_data="L"),
        ],
    ]
)



LOG_TEXT = """
     ● ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ●

 ❥︎ ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴀɴʏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴜsɪɴɢ 
 ❥︎ ᴛʜᴇɪʀ ᴘʏʀᴏɢʀᴀᴍ ᴏʀ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ.
 ❥︎ ᴏᴡɴᴇʀ : 𝐀ʟᴘʜᴀ 𝐁ᴀʙʏ
"""

ALPHA_MODS = IKM(
    [
        [
            IKB("𝗔", callback_data="A"),
            IKB("𝗕", callback_data="B"),
            IKB("𝗖", callback_data="C"),
            IKB("𝗗", callback_data="D"),
        ],
        [
            IKB("𝗘", callback_data="E"),
            IKB("𝗙", callback_data="F"),
            IKB("𝗚", callback_data="G"),
            IKB("𝗛", callback_data="H"),
        ],
        [
            IKB("𝗜", callback_data="I"),
            IKB("𝗝", callback_data="J"),
            IKB("𝗞", callback_data="K"),
            IKB("𝗟", callback_data="L"),
        ],
        [
            IKB("⬅️ ʙᴀᴄᴋ", callback_data="back_btn"),
        ],
    ]
)

