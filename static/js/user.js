document.addEventListener("DOMContentLoaded", function () {
    // 1. Toast xabarni avto-yopish
    const toastContainer = document.getElementById("toast-container");
    if (toastContainer) {
        setTimeout(function () {
            toastContainer.style.animation = "fadeOut 0.5s ease forwards";
            setTimeout(function () { toastContainer.remove(); }, 500);
        }, 3500);
    }

    // TYPEWRITER ENGINE (Universal yozish funksiyasi)
    function typeText(elementId, cursorId, text, speed, callback) {
        let i = 0;
        const el = document.getElementById(elementId);
        const cursor = document.getElementById(cursorId);

        function typing() {
            if (i < text.length) {
                el.innerHTML += text.charAt(i);
                i++;
                setTimeout(typing, speed);
            } else {
                if (cursor) cursor.style.display = "none"; // Yozib bo'lingach kursor yo'qoladi
                if (callback) callback();
            }
        }
        typing();
    }

    // MATNLAR BAZASI
    const title1Text = "Life GYM sizga yordam beradi!";
    const leadText = "bu zamonaviy texnologiyalar hamda sun'iy intellekt (AI) imkoniyatlarini birlashtirgan raqamli fitness va salomatlik ekotizimidir. Platforma sizning shaxsiy ko'rsatkichlaringizni tahlil qilib, sog'lom va tartibli turmush tarziga tez hamda to'g'ri moslashishingizga ko'maklashadi.";
    const title2Text = "📌 Platforma sizga qanday masalalarda yordam beradi?";

    const listData = [
        "<strong>Shaxsiy AI Diyetolog va Maslahatchi:</strong> Vazn tashlash, mushak massasini oshirish yoki jismoniy holatni saqlash bo'yicha sun'iy intellektga asoslangan tahlillarni beradi.",
        "<strong>To'g'ri ovqatlanish va BJU balansi:</strong> Organizm uchun zarur bo'lgan kunlik oqsil, yog' va uglevodlar (BJU) miqdorini aniq hisoblab beradi.",
        "<strong>Individual rejalashtirish:</strong> Maqsadingizga mos ravishda kunlik, haftalik hamda oylik shaxsiy fitness va mashq rejalarini shakllantiradi.",
        "<strong>Intellektual progress tahlili:</strong> Bajarilgan mashg'ulotlar hamda natijalaringizni doimiy ravishda monitoring qilib borishingizni ta'minlaydi.",
        "<strong>Suv va kunlik energiya nazorati:</strong> Kun davomida qabul qilinishi kerak bo'lgan suv balansi hamda metabolizmni nazorat qilishga yordam beradi.",
        "<strong>Vaqt va mablag' tejash:</strong> Qimmatli vaqtingizni tejab, istalgan joyda shaxsiy virtual murabbiyga ega bo'lasiz."
    ];

    // ZANJIRSIMON KETMA-KET YOZISH JARAYONI
    // 1-bosqich: Bosh sarlavha yoziladi
    typeText("type-title1", "cursor-title1", title1Text, 25, function () {

        // 2-bosqich: Kirish matni paydo bo'ladi va harfma-harf yoziladi
        const leadBox = document.getElementById("lead-box");
        if (leadBox) leadBox.style.display = "block";

        typeText("type-lead", "cursor-lead", leadText, 15, function () {

            // 3-bosqich: Ikkinchi sarlavha ("📌 Platforma sizga qanday masalalarda...") yoziladi
            const sectionBox = document.getElementById("section-box");
            if (sectionBox) sectionBox.style.display = "block";

            typeText("type-title2", "cursor-title2", title2Text, 20, function () {

                // 4-bosqich: Ro'yxat elementlari harfma-harf birma-bir yoziladi
                typeListItems(0);
            });
        });
    });

    // RO'YXATNI HARFMA-HARF YOZISH FUNKSIYASI
    function typeListItems(index) {
        if (index >= listData.length) return;

        const listContainer = document.getElementById("write-list");
        const li = document.createElement("li");

        const textSpanId = "list-text-" + index;
        const cursorId = "list-cursor-" + index;

        li.innerHTML = `<span id="${textSpanId}"></span><span class="cursor" id="${cursorId}">|</span>`;
        listContainer.appendChild(li);

        let htmlText = listData[index];
        let el = document.getElementById(textSpanId);
        let cursor = document.getElementById(cursorId);
        let i = 0;

        function typeChar() {
            if (i < htmlText.length) {
                // HTML teglarni (<strong>) tez o'tkazish
                if (htmlText.charAt(i) === '<') {
                    let tagCloseIndex = htmlText.indexOf('>', i);
                    i = tagCloseIndex + 1;
                } else {
                    i++;
                }
                el.innerHTML = htmlText.substring(0, i);
                setTimeout(typeChar, 10);
            } else {
                if (cursor) cursor.style.display = "none";
                typeListItems(index + 1); // Keyingi ro'yxat punktiga o'tish
            }
        }
        typeChar();
    }
});