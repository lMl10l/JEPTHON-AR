from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 

JMTHON = ("الامر 1")
CATAR = ("الامر 2")
RRRD7 = ("الامر 3")  ##Arabic Cat by  - @RRRD7.- @UUNZZ

@borg.on(admin_cmd("الاوامر"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- هذه هي قائمة اوامر البوت الخاصة بك\n\n**  لعرض اوامر الكتم والحظر ارسل `.الامر 1` \n لعرض اوامر المجموعة ارسل `.الامر 2`\n لعرض اوامر الترحيب ارسل `.الامر 3`\n لعرض اوامر اضافة الردود ارسل `.م4`\n لعرض اوامر حماية الخاص ارسل  `.م5` \n لعرض اوامر التلكراف ارسل `.م6`\nلعرض اوامر صلاحيات الكروب ارسل `.م7`\nلعرض اوامر التاك والابلاغ ارسل `.م8`\nلعرض اوامر الكشف والايدي ارسل `.م9`\nلعرض اوامر تحويل الصيغ ارسل `.م10`\n لعرض اوامر الترجمه ارسل `.م11`\nلعرض اوامر البحث والتحميل ارسل `.م12`\nلعرض اوامر الانتحال ارسل `.م13`\nلعرض اوامر التشغيل ارسل `.م14`\nلعرض اوامر المنع ارسل `.م15`\nلعرض اوامر التسلية ارسل `.م16`\nلعرض اوامر التنظيف والتنصيب ارسل `.م17`\nلعرض اوامر البروفايل الوقتي ارسل `.م18` \n لعرض اوامر التقليد ارسل `.م19`\n لعرض اوامر اخرى ارسل `.م20`\nلعرض اوامر الفارات وهيروكو ارسل `.م21`\n لعرض اوامر الملصقات ارسل `.م22`\nلعرض اوامر معلومات الكروب ارسل `.م23`\n لعرض اوامر الروابط ارسل `.م24`\n لعرض اوامر الكروب الثانية ارسل `.م25`\n لعرض اوامر التخصيص ارسل `.م26`\nلعرض الاوامر الثانوية ارسل `.م27`\n لعرض اوامـر الهمسة واكس او ارسل `.م28`\n\n [⌔︙قناة السورس](t.me/JMTHON)" ) 
        
@borg.on(admin_cmd(JMTHON))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(" - اوامر الـحظر و الكتم\n\n**هنالك بعض الاوامر تشتغيل بالرد او بوضع الايدي او بوضع** المعرف\n\n────────────────\n\nالأمر  𖥻  `.كتم`   + سبب الكتم غير اجباري\nاستخدامه  𖥻 لكتم شخص عام في جميع المجموعات \n────────────────\n\nالامر  𖥻  `.الغاء كتم`\nاستخدامه   𖥻  لالغاء كتم الشخص والسماح له بالتحدث \n────────────────\n\nالامر  𖥻 `.حظر`  + السبب | غير اجباري\nاستخدامه  𖥻 لحظر شخص من جميع المجموعات\n────────────────\n\nالامر  𖥻 `.طرد`  + السبب | غير اجباري\nاستخدامه  𖥻 لطرد شخص من مجموعة معينة\n────────────────\n\nالامر  𖥻  `.كتم_مؤقت`  | + الوقت \nاستخدامه  𖥻 لكتم شخص مؤقتا في الكروب \nالخيارات  𖥻  بالدقائق  = m  | بالثواني  = s  | بالساعات  = h \nمثال  𖥻 [اضغط هنا](https://t.me/Jmthon_tools/243)\n────────────────\nالامر  𖥻  `.حظر_مؤقت`   | + الوقت \nاستخدامه  𖥻 لحظر شخص مؤقتا في الكروب \nالخيارات  𖥻  بالدقائق  = m  | بالثواني  = s  |\nبالساعات  = h\nمثال  𖥻 انقر هنا\n────────────────\n [⌔︙قناة السورس](t.me/JMTHON)" ) 
        
@borg.on(admin_cmd(CATAR))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("- اوامر المجموعة \n\n**تذكـر قبل ارسال الامر يجب وضع نقطة وبعدها الامر وتذكر ان بعض الاوامر يشتغلن بالرد على الشخص او وضع ايديه مع الامر او معرفه**\n\n────────────────\n\nالأمر  𖥻  `.رفع مشرف`   \nاستخدامه  𖥻 لرفع شخص مشرف في المجموعه مع بعض الصلاحيات\n────────────────\n\nالامر  𖥻  `.تك`\nاستخدامه   𖥻  لحذف جميع صلاحيات الشخص من الاشراف\n────────────────\n\nالامر  𖥻 `.تثبيت`  + بالأشعار | لعمل اشعار\nاستخدامه  𖥻 لتثبيت رسالة في المجموعه\n────────────────\n\nالامر  𖥻 `.الغاء التثبيت`  + للكل | لالغاء تثبيت الرسائل\nاستخدامه  𖥻 لالغاء تثبيت رسالة معينة او كل الرسائل \n────────────────\n\nالامر  𖥻  `.الاحداث`  |  ر-  + رقم من 1 الى 15\nاستخدامه  𖥻 لعرض الرسائل المحذوفة يتطلب صلاحيات\nملاحظة  𖥻   .الاحداث ر-  15 سيقوم بعرض الاحداث رسالة رسالة ويرد على الامر \n────────────────\n\nالأمر  𖥻  `.ضع تكرار`   + رقم تكرار\nاستخدامه  𖥻 لوضع تكرار اذا شخص تجاوز التكرار سيتم كتمه\n──────────────── \n [⌔︙قناة السورس](t.me/JMTHON)") 

@borg.on(admin_cmd(RRRD7))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("- اوامر الترحيب  \n** اوامر الترحيب فقط اكتبها بالمجموعات ليقوم بترحيب بالمستخدمين الجدد **\n\n────────────────\n\nالامر  𖥻 `.ترحيب`   +  الترحيب\nمثال 𖥻 .ترحيب - ههـلـو عـمـري ♥َ🦋ِ . \n────────────────\n\nالامر  𖥻  `.حذف الترحيبات`\nالشرح  𖥻  لحذف جميع الترحيبات لمجموعه معينة\n────────────────\n\nالامر  𖥻 `.الترحيبات`\nالشرح  𖥻  يقوم بعرض الترحيب المضاف لمجموعة معينة\n────────────────\n [⌔︙قناة السورس](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م4"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("- اوامر الردود \n\nالامر  𖥻 `.اضف رد`\nالشرح 𖥻 شاهد شرح توضيحي [اضغط هنا](https://t.me/Jmthon_tools/242)\n────────────────\n\nالامر  𖥻  `.حذف رد`  |  + الرد\nالشرح  𖥻  لحذف رد معين من دردشه معينة \n────────────────\n\nالامر  𖥻  `.الردود` \nالشرح  𖥻  يقوم بعرض الردود الي تم اضافتها\n──────────────── \n\nالامر  𖥻  `.حذف الردود`\nالشرح  𖥻 يقوم بحذف جميع الردود المضافه للدردشة\n────────────────\n [⌔︙قناة السورس](t.me/JMTHON)")
        
@borg.on(admin_cmd("م5"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(" - اوامر الحماية\n\nالامر  𖥻 .الحماية on/off \nالاستخدام  𖥻 كتابه الامر مع on لتشغيله و off لتعطيله \n الشرح 𖥻 يستخدم هذا الامر لتفعيل خاصية حماية الخاص \n──────────────── \n\n الامر  𖥻 .سماح   او  .س \nاستخدامه  𖥻  للموافقه على الشخص وجعله يتكلم بحرية في الخاص \n────────────────\n\nالامر  𖥻  .رفض  او  .ر \n استخدامه  𖥻  يقوم برفض الشخص من الخاص واذا كرر سيتم حظره تلقائيا\n ────────────────\n\nالامر  𖥻 .بلوك \n استخدامه 𖥻 يستخدم هذا الامر لحظر شخص من الخاص فقط قم بالرد عليه\n────────────────\n\nالامر  𖥻 .انبلوك \n استخدامه  𖥻  يستخدم هذا الامر لحظر شخص من الخاص فقط قم بالرد عليه \n────────────────\n\nالامر  𖥻  .المسموح لهم\n استخدامه  𖥻  يقوم بعرض قائمه الاشخاص الذي تم الموافقة عليهم والذي تم رفضهم من الخاص\n────────────────\n [⌔︙قناة السورس](t.me/JMTHON)")
        
@borg.on(admin_cmd("م6"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر التلكراف** \n\nالامر  𖥻  `.تلكراف t`\n الاستخدام 𖥻  ليقوم بصنع رابط تلكراف لمقالة او موضوع معين \nالشرح  𖥻  قم بالرد على النص المراد تحويله الى رابط تلكراف\n────────────────\n\nالامر  𖥻  `.تلكراف m` \nالاستخدام  𖥻  ليقوم بصنع رابط تلكراف لصورة او فيديو او متحركه\nالشرح  𖥻  قم بالرد على الصورة المراد تحويلها الى رابط تلكراف\n──────────────── \n [⌔︙قناة السورس](t.me/JMTHON)")
        
@borg.on(admin_cmd("م7"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر قفل وفتح الصلاحيات** \n\nالامر  𖥻  .قفل + الاضافة   |  .فتح  + الاضافة\nالاستخدام  𖥻 تكتب قفل مع الاضافه لقفل شي من المجموعه ولفتحه ارسل  فتح مع الاضافه لفتحه\nملاحظة  𖥻 لرؤية الاضافات [اضغط هنا](https://t.me/Jmthon_tools/143)\n────────────────\n [⌔︙قناة السورس](t.me/JMTHON)")
        
@borg.on(admin_cmd("م8"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر المنشن  والتاك**\n\nالامر  𖥻 .تاك  + معرف الشخص  + الرسالة\nالشرح  𖥻 لعمل تاك لشخص ووضع التاك داخل الرسالة شاهد المثال وجرب بنفسك\nمثال 𖥻 .تاك @RRRD7  ههلا\n────────────────\n\nالامر  𖥻  `.للكل`  + الرسالة\nالاستخدام 𖥻  لعمل تاك للكل مع الرسالة\nمثال 𖥻  .للكل هههلا\n────────────────\n\nالامر  𖥻  `.ابلاغ`\nالشرح  𖥻  سيقوم بعمل تاك لمشرفين المجموعه\n────────────────\n [⌔︙قناة السورس](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م9"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الكشف\n**تستخدم اوامر الكشف  بالرد على الشخص او وضع معرفه او ايديه مع الامر**\n\nالامر  𖥻 `.الايدي` \nالشرح  𖥻 لاظهار ايدي الشخص و المجموعه فقط قم بالرد على الشخص \n────────────────\n\nالامر  𖥻  `.ايدي` \nالشرح  𖥻 يقوم باظهار معلومات عن الشخص \n────────────────\n\nالامر  𖥻  `.رابط الحساب` \nالشرح  𖥻  سيقوم بعمل رابط لحساب الشخص \n────────────────\n [⌔︙قناة السورس](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م10"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر تحويل الصيغ**\n\nالامر 𖥻 `.تحويل صورة`\nالاستخدام  𖥻 الرد على الملصق لتحويله صورة \n────────────────\n\nالامر  𖥻  `.تحويل ملصق`\nالاستخدام 𖥻  بالرد على الصورة لتحويله ملصق \n────────────────\n\nالامر  𖥻  `.تحويل متحركه`\nالاستخدام  𖥻 بالرد على الملصق المتحرك لتحويله متحركه \n──────────────── \n\nالامر  𖥻  `.تحويل voice `\nالاستخدام  𖥻 بالرد على الاغنيه لتحويلها على شكل بصمة \n──────────────── \n\nالامر  𖥻  `.تحويل mp3`\nالاستخدام  𖥻 بالرد على البصمه او المقطع الصوتي لتحويله على شكل اغنية \n──────────────── \n الامر𖥻  `.تحويل نص`\nالاستخدام  𖥻 يقوم بتحويل النص الى ملصق \n──────────────\n\n[⌔︙قناة السورس](t.me/JMTHON)")
@borg.on(admin_cmd("م11"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر الترجمه \n\nالامر  𖥻 `.ترجمه ar`    |  `.ترجمه en \n`الاستخدام  𖥻 ترد على النص المراد ترجمته \nالشرح 𖥻  اذا تريد ترجمه من اي لغة للعربية رد على الرسالة بـ `.ترجمه ar`  \n\n────────────────\n [⌔︙قناة السورس](t.me/JMTHON)")
  
@borg.on(admin_cmd("م12"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر البحث والتحميل  \n\nالامر  𖥻 `.بحث` \nالاستخدام  𖥻 كتابة اسم الاغنية مع الامر لارسال الاغنيه لك \n────────────────\n\nالامر  𖥻  `.سكرين `\nالاستخدام 𖥻  بكتابة رابط الموقع مع الامر لاخذ ضورة وارسالها لك \n──────────────── \n\nالامر 𖥻 `.يوت` + العنوان\n استخدامه 𖥻 تقوم بكتابه الامر مع عنوان الفيديو او الاغنية المطلوبة وسيرسلك روابط البحث لاستخدامه في التحميل\n──────────────── \n\n الامر 𖥻 `.تحميل ص`  + الرابط\n استخدامه 𖥻 لتحميل اغنيه من خلال وضع الرابط مع الامر\n──────────────── \n\n الامر 𖥻 `.تحميل ف`  + الرابط\n استخدامه 𖥻 كتابة الامر مع رابط المقطع لتحميله وارساله لك\nالامر 𖥻 `.انستا`  + الرابط\nاستخدامه 𖥻 يستخدم هذا الامر لتحميل من الانستا فقط اكتب الامر مع رابط الفيديو ليحمله\n\n [⌔︙قناة السورس](t.me/JMTHON)")
        
@borg.on(admin_cmd("م13"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر  الانتحال** \n\nالامر  𖥻 `.انتحال`  \nالاستخدام 𖥻  لنسخ حساب الشخص بالكامل من صورة اسم وبايو..... والخ \n──────────────────\n\nالامر  𖥻 `.اعادة`  \n`الاستخدام 𖥻   لاعادة الحساب كما كان بالاول \n **ملاحظة  𖥻 تستخدم اوامر الانتحال بالرد على الشخص او وضع ايدي الشخص او معرفه**\n─────────────────\n\n   [⌔︙قناة السورس](t.me/JMTHON)")
               
        
@borg.on(admin_cmd("م14"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر التشغيل والايقاف \n\nالامر  𖥻 `.اعادة تشغيل`  \nالاستخدام  𖥻 فقط اكتب الامر ليقوم بأعادة تشغيل البوت \n─────────────\n\nالامر  𖥻 `.ايقاف`\nالشرح 𖥻   لايقاف البوت عن التشغيل ولاعادة تشغيله التنصيب من جديد \n─────────────\n\n  [جـمثون هنا](t.me/JMTHON)")

@borg.on(admin_cmd("م15"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر القائمة السوداء**  \n\nالامر  𖥻 `.منع` \nالاستخدام  𖥻 اكتب الامر مع الكلمه المراد منعها ليقوم البوت بحذفها في دردشه معينة \n───────────\n\nالامر  𖥻  `.الغاء منع`\nالاستخدام 𖥻  اكتب الامر مع الكلمة الذي تم منعها للسماح للكلمه وعدم حذفها\n ─────────────\n\nالامر  𖥻  `.القائمة السوداء` \nالشرح  𖥻  يقوم بأظهار الكلمات الذي تم منعها من الدردشة \n───────────── \n\n [⌔︙قناة السورس](t.me/JMTHON)")
        
@borg.on(admin_cmd("م16"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**-  اوامر التسليه :\n\n فقط ارسل الامر وجربه **\n𖥻 `.قمر`\n𖥻 `.اقمار`\n𖥻 `.قمور`\n𖥻 `.قلوب`\n𖥻 `.قلب `\n𖥻 `.جيم`\n𖥻 `.افكر`\n𖥻 `.افكرر`\n𖥻 `.شنوو `\n𖥻 `.مح `\n𖥻 `.متت `\n𖥻 `.النضام الشمسي `\n𖥻 `.موسيقى `\n𖥻 `.قنبله `\n𖥻 `.مكبعات `\n𖥻 `.افعى `\n𖥻 `.طائره `\n𖥻 `.نجمه `\n𖥻 `.دائره `\n𖥻 `.شرطه `\n𖥻 `.فايروس `\n𖥻 `.غبي `\n𖥻 `.العد التنازلي`\n - `.يد`\n - `.تهكير`\n - `.قرد `\n - `.بشره `\n - `.انيم `\n - `.نيكول `\n - `.مربع`\n - `.قاتل `\n - `.تحميل`\n - `.رجل `\n - `.شنوو `\n - `.ريبي `\n - `.تفريغ `\n - `.حلويات `\n - `.فليم`\n\n -  [⌔︙قناة السورس](t.me/JMTHON)")
        
@borg.on(admin_cmd("م17"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر التنظيف والتنصيب** \n\nالامر 𖥻 `.تكرار `\nالاستخدام  𖥻  بكتابة الامر مع الرقم و الكلمة او النص لتكرارها \nمثال 𖥻 .تكرار 10 جمثون\n─────────────\n\nالامر  𖥻   `.سبام` \nالاستخدام 𖥻 بكتابة الكلمة مع الامر ليقوم بتفصيخ الحروف وارسالها \n─────────────\n\nالامر  𖥻   `.تنصيب` \nالاستخدام  𖥻   بكتابة الامر بالرد على الملف لتنصيبه للبوت\n─────────────\n\nالامر  𖥻   `.الغاء التنصيب` \nالاستخدام  𖥻   بكتابة الامر مع اسم الملف لحذف هذا الامر من البوت لمدة 24 ساعة\n─────────────\n\nالامر 𖥻  `.تنظيف` \n\nالاستخدام 𖥻  يقوم بحذف الرسائل اكتب الامر على رسالة معينة وسيقوم بحذف الرسائل التي تحتها بروفايلك\n\n────────────\n\nالامر  𖥻   `.مسح`  \nالاستخدام  𖥻  فقط اكتب الامر بالرد على الرسالة ليقوم بحذفها \n────────────\n\n [⌔︙قناة السورس](t.me/JMTHON)")

@borg.on(admin_cmd("م18"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر البروفايل التلقائي** \n\nالامر  𖥻 `.اسم وقتي ` \nالاستخدام 𖥻 فقط ارسل الامر لجلعل اسمك يتغير كل دقيقه مع تغير الوقت   \n───────────\n\nالامر  𖥻  `.بايو وقتي`\nالاستخدام 𖥻  فقط اكتب الامر لعرض تاريخ يتغير مع النبذة \n ───────────\n\nالامر  𖥻  `.انهاء + الامر`\nالاستخدام  𖥻  يقوم بايقاف الامر من قائمه الوقتي فقط كالأسم الوقتي او النبذة الوقتية \nمثال 𖥻 .انهاء اسم وقتي \n─────────── \n [⌔︙قناة السورس](t.me/JMTHON)")

@borg.on(admin_cmd("م19"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر تقليد الشخص** \n- ملاحظة 𖥻 اوامر التقليد تشتغل بالرد على الشخص  او كتابة ايدي الشخص مع الامر او معرفه \n\nالامر  𖥻 `.تقليد` \nالاستخدام  𖥻 بالرد على الشخص ليقوم بتكرار جميع رسائل الشخص الذي فعلت عليه الامر \n───────────\n\nالامر  𖥻  `.الغاء التقليد `\nالاستخدام 𖥻 لالغاء تقليد الشخص وعدم ارسال رسائله\n ───────────\n\nالامر  𖥻  `.المقلدهم` \nالاستخدام  𖥻  فقط اكتب الامر ليقوم بعرض الاشخاص الي تم تقليدهم\n─────────── \n\n [⌔︙قناة السورس](t.me/JMTHON)")

@borg.on(admin_cmd("م20"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- الاوامر الاخرى** \n- **ملاحظة 𖥻 لاستخدام امر نقل الملكية تحتاج لوضع `TG_2STEP_VERIFICATION_CODE` و معه رمز حسابك في الفارات** \n\nالامر  𖥻 `.ملكية` \nالاستخدام  𖥻 يجب عليك كتابة التمر في القناه التي تريد تحويلها لشخص وبكتابه الامر مع معرف الشخص  \n───────────\n\nالامر  𖥻  `.لستة `\nالاستخدام 𖥻 يقوم بصنع لستة شفافة لمنشور معين شاهد الشرح [اضغط هنا](https://t.me/Jmthon_tools/202) \n الامر 𖥻 `.الوقت`\n الاستخدام 𖥻 فقط ارسل الامر وسيعرض لـك توقيت بلدك على ملصق\n ───────────\n\nالامر  𖥻  `.تحذير`  + السبب \nالاستخدام  𖥻 بالرد على الشخص ليقوم بتحذيره \n الامر 𖥻 `.التحذيرات` \nالاستخدام  𖥻 بالرد على الشخص ليقوم باظهار تحذيراته  \n────────────\n\nالامر 𖥻 `.حذف التحذيرات` \nالاستخدام  𖥻 بالرد على الشخص لحذف تحذيراته \n───────────── \n\nالامر 𖥻 `.تطبيق` \n استخدامه كتابة الامر مع اسم تطبيق او لعبه وسيعطيك تفاصيلها ورابط تنزيل من سوق بلي \n\n  [⌔︙قناة السورس](t.me/JMTHON)")

@borg.on(admin_cmd("م21"))
async def _(event):  # كتابة الملف بواسطه  : @RRRD7 - and @UUNZZ
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر هيروكو والفارات** \n\nالامر  𖥻  `.استخدامي` \nالاستخدام  𖥻 ارسل الامر فقط لعرض مدة  استخدام للسورس والساعات المتبقية\n───────────\n\nالامر  𖥻  `.الدخول` \nالاستخدام 𖥻  فقط اكتب الامر لعرض اخر 100 سطر من تطبيق هيروكو الي نصبت عليه\n─────────── \n\n [⌔︙قناة السورس](t.me/JMTHON)")

@borg.on(admin_cmd("م22"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر الملصقات :** \nالامر: 𖥻 `.ملصق ` \n الاستخدام 𖥻 بالرد على الملصق لأخذه وعمل حزمه واضافته به ──────────\n الامر 𖥻 `.حزمة` \n الاستخدام 𖥻 بالرد على الملصق لنسخ الحزمه كامل ──────────ا \n الامر 𖥻 `.معلومات_الملصق`\n الاستخدام 𖥻 بالرد على الملصق لعرض معلومات الحزمة────────── \n\n [⌔︙قناة السورس](t.me/JMTHON)")

@borg.on(admin_cmd("م23"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**اوامر معلومات الكروب** \n\nالامر  𖥻 `.معلومات_الدردشة` \nالاستخدام  𖥻 ارسال الامر في المجموعه لرؤية معلومات المجموعه\n─────────────\n\nالامر  𖥻 `.البوتات` \nالاستخدام 𖥻 ارسل الامر لرؤية بوتات الموجوده في المجموعه\n\n─────────────\n\nالامر  𖥻  `.المشرفين` \nالاستخدام  𖥻 كتابة الامر فقط في المجموعه لرؤية مشرفين الكروب \n────────────── \n\nالامر  𖥻  `.الاعضاء` \nالاستخدام  𖥻 كتابة الامر فقط لرؤية معرفات اعضاء الكروب\n────────────── \n\n [⌔︙قناة السورس](t.me/JMTHON)")
                
@borg.on(admin_cmd("م24"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر الروابط**\n\n الامر 𖥻 `.دنس`  + الرابط\n استخدامه 𖥻 لكشف معلومات نظام دومين موقع معين اكتب الامر مع الرابط\n──────────────\n\n الامر 𖥻 `.مصغر` \n\n استخدامه  𖥻 بالرد على الرابط او وضع الرابط مع الامر ليقوم بتصغيره \n────────────────\n\n الامر 𖥻 `.رابط_مخفي` \n استخدامه  𖥻 بالرد على الرابط لاخفاء الرابط وجعله في مسافه معينه جرب الامر بنفسك\n─────────────────\n\n [⌔︙قناة السورس](t.me/JMTHON)")
        
@borg.on(admin_cmd("م25"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**اوامر الكروب الثانية** \n\nالامر  𖥻 `.اطردني` \nالاستخدام  𖥻 ارسال الامر في المجموعه ليقوم بالمغادرة\n───────────\n\nالامر  𖥻 `.طرد_الكل` \nالاستخدام 𖥻 ارسل الامر لطرد جميع الاعضاء من المجموعه\n\n───────────\n\nالامر  𖥻  `.حظر_الكل` \nالاستخدام  𖥻 كتابة الامر فقط في المجموعه لحظر جميع الاعضاء \n─────────── \n\nالامر  𖥻  `.الغاء الحظر للكل` \nالاستخدام  𖥻 كتابة الامر في الكروب لالغاء حظر جميع الاعضاء\n──────────\n\n الامر 𖥻 `.المحذوفين` \n استخدامه 𖥻 لعرض الحسابات المحذوفة في المجموعة ولحذفهم ارسل `.المحذوفين اطردهم` \n\n [⌔︙قناة السورس](t.me/JMTHON)")

@borg.on(admin_cmd("م26"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- اوامر التخصيص**'\n\nالامر  𖥻 `.تخصيص pmpermit`\nالاستخدام  𖥻 بالرد على الرسالة التي تريد وضعها رسالة تحذيرات لامر حماية الخاص\n───────────\n\nالامر  𖥻  `.تخصيص pmpic` \nالاستخدام 𖥻  بالرد على رابط الصورة  لوضع صورة مع امر حمايه الخاص قم بالرد على رابط صورة من تلكراف ولـتحويل الصورة الى رابط تلكراف قم بالرد على الصورة  `.تلكراف m`\n ───────────\n\nالامر  𖥻  `.تخصيص pmblock` \nالاستخدام  𖥻 يستخدم هذا الامر لوضع رسالة الحظر التي ترسل بعدما الشخص يقوم بتكرار الرسائل في الخاص قم بالرد على الرسالة التي تريد وضعها بالامر \n الامر 𖥻 `.تخصيص startmsg` \n استخدامه 𖥻 بالرد على الرسالة التي تريدها تظهر بعدما الشخص يشغل بوتك \n─────────── \n\n ⌔︙قناة السورس [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 

@borg.on(admin_cmd("م27"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**-الاوامر الثانوية** \n\nالامر  𖥻 `.صوره` \nالاستخدام  𖥻 بالرد على الشخص للحصول على صورة حسابه الشخصيه واذا تريد جميع صور حسابه قم بالرد عليه بـ `.صوره كلها` \n───────────\n\nالامر  𖥻 `.سرعة الانترنت` \nالاستخدام 𖥻 ارسل الامر لقياس سرعة الانترنت\n\n───────────\n\nالامر  𖥻  `.حساب` \nالاستخدام  𖥻 كتابة الامر مع معادلة رياضيات وسيقوم بحلها وارسالها لك \n─────────── \n\nالامر  𖥻  `.تاريخ` \nالاستخدام  𖥻 بالرد على الشخص او كتابة معرفه مه الامر لعرض سجل اسماء حسابه \n──────────\n\n الامر 𖥻 `.الوقت` \n استخدامه 𖥻 لعرض الوقت على شكل ملصق \n──────────\n\n الامر 𖥻 `.وقت` \n استخدامه 𖥻 لعرص الوقت والتاربخ على شكل كتابة \n───────────\n\n الامر 𖥻 `.صلاة`  \n استخدامه 𖥻 اكتب الامر مع اسم محافظتك باللغه الانكليزية للحصول على اوقات الصلاة \n───────────\n\n[⌔︙قناة السورس](t.me/JMTHON)")
        
        
