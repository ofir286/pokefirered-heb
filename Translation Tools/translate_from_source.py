import re
import sys

HEB_REGEX        = r"(\w+::\n.+?(?:(?:done)|(?:text_end)|(?:prompt)))"
INNER_TEXT_REGEX = r'"(.+)"'
LINE_FORAMT      = '    .string "{0}{1}"'
MERGE_FORMAT     = '    .string "{0}{1}{2}"'
WORD_SWITCH_DICT =\
{
    "אלון" : "אוק",
    "#" : "פוק",
    "פוכדור" : "פוקיבול",
    "פוקידע" : "פוקדקס",
    "<" : "{",
    ">" : "}",
    "@" : "{}",
    "מוזרע" : "בלבאזור",
    "דשונה" : "אייויזור",
    "פרחריג" : "וינאזור",
    "גחומט" : "צ'רמנדר",
    "חזיזיקית" : "צ'רמיליון",
    "לטאש" : "צ'ריזארד",
    "שפריצב" : "סקווירטל",
    "קרבצב" : "וורטורטל",
    "מפציצב" : "בלסטויז",
    "זחי" : "קטרפי",
    "מפקעת" : "מטפוד",
    "פרפרץ" : "בטרפרי",
    "תולחט" : "ווידל",
    "גלגולם" : "קאקונה",
    "מקדבור" : "בידריל",
    "יונדי" : "פידג'י",
    "יונה-עשרה" : "פידג'יוטו",
    "סילונה" : "פידג'יוט",
    "עכברסס" : "רטטה",
    "הדברוש" : "רטיקייט",
    "כידרור" : "ספירו",
    "פחדרור" : "פירו",
    "שחן" : "אקנס",
    "נתף" : "ארבוק",
    "צויצוץ" : "פיקאצ'ו",
    "עכברעם" : "ראיצ'ו",
    "חולדף" : "סנדשרו",
    "חותחול" : "סנדסלאש",
    "מחטנית♀" : "נידורן♀",
    "חודנית" : "נידורינה",
    "מלכצת" : "נידוקווין",
    "מחטן♂" : "נידורן♂",
    "חודן" : "נידורינו",
    "מלקץ" : "נידוקינג",
    "חמשדון" : "קלפרי",
    "חמשל" : "קלפייבל",
    "ששועל" : "וולפיקס",
    "תשעלים" : "ניינטיילס",
    "ניענפוח" : "ג'יגליפאף",
    "כישקשוח" : "וויגליטאף",
    "אצלף" : "זובאט",
    "בלעלף" : "גולבאט",
    "צנוזר" : "אודיש",
    "פריכאון" : "גלום",
    "עשנבל" : "ויילפלום",
    "טפל" : "פרס",
    "טפרק" : "פרסקט",
    "רעלתוש" : "ונונאט",
    "רעלעש" : "ונומות'",
    "חפיד" : "דיגלט",
    "חפליה" : "דאגטריו",
    "מיצי" : "מיאו",
    "קיצי" : "פרסיאן",
    "תקשורווז" : "פסיידאק",
    "ברווזהב" : "גולדאק",
    "קופבני" : "מאנקי",
    "קופזועם" : "פריימיפ",
    "נהמיש" : "גראולית'",
    "כלבזק" : "ארקניין",
    "ראשנע" : "פוליוואג",
    "ראשבוב" : "פוליוורל",
    "ראשזעם" : "פוליראת'",
    "אברא" : "אברה",
    "כדברא" : "קדברה",
    "אוגלר" : "אלקזם",
    "גברכה" : "מאצ'ופ",
    "גברנק" : "מאצ'וק",
    "גברלוף" : "מאצ'אמפ",
    "פעמוניצן" : "בלספראוט",
    "דמעמון" : "וויפינבל",
    "תהילעמון" : "ויקטריבל",
    "קרשוש" : "טנטקול",
    "מרושוש" : "טנטקרול",
    "בחורקע" : "ג'יאודוד",
    "מחצץ" : "גרבלר",
    "גוילם" : "גולם",
    "סיחום" : "פוניטה",
    "סוסורף" : "רפידאש",
    "כיסלאט" : "סלופוק",
    "אחלאט" : "סלוברו",
    "שואבן" : "מגנמייט",
    "קוטבת" : "מגנטון",
    "לוסביר" : "פארפג'ד",
    "שנישליו" : "דודו",
    "שלושליו" : "דודריו",
    "נבים" : "סיל",
    "טלחש" : "דיוגונג",
    "טנפאי" : "גריימר",
    "מרפש" : "מאק",
    "קונכך" : "שלדר",
    "מבוצדף" : "קלויסטר",
    "שאד" : "גסטלי",
    "רוצד" : "האנטר",
    "אשלדאי" : "גנגר",
    "נחשוהם" : "אוניקס",
    "ישנום" : "דראוזי",
    "מושין" : "היפנו",
    "שרטני" : "קראבי",
    "כנרטן" : "קינגלר",
    "חשמלמל" : "וולטורב",
    "מוקשמל" : "אלקטרוד",
    "ביצמודות" : "אקזגקיוט",
    "תמרצח" : "אקזגקיוטור",
    "רשרש" : "קיובון",
    "קרקש" : "מארוואק",
    "הכמפמדג" : "היטמונלי",
    "הכמפארד" : "היטמונצ'אן",
    "עגולשון" : "ליקיוטנג",
    "משתעשן" : "קופינג",
    "משתעשניים" : "ויזינג",
    "קרנוזף" : "רייהורן",
    "קרנשיא" : "ריידון",
    "בת-מזל" : "צ'נסי",
    "סבכיה" : "טנגלה",
    "כיסבל" : "קנגסקאן",
    "ימסוס" : "הורסי",
    "אץ-ים" : "סידרה",
    "זהלכה" : "גולדין",
    "ימלך" : "סיקינג",
    "כוכיש" : "סטאריו",
    "כוכשיט" : "סטארמי",
    "מרחקיין" : "מר. מיים",
    "מגל-שלמה" : "סייטר",
    "בישה" : "ג'ינקס",
    "חשמזום" : "אלקטאבאז",
    "לברווז" : "מגמר",
    "צבתן" : "פינסיר",
    "פרסוס" : "טאורוס",
    "קסמנון" : "מג'יקארפ",
    "לויטורף" : "גרידוס",
    "תכוגית" : "לפרס",
    "שינוץ" : "דיטו",
    "פאתו" : "איווי",
    "אדידן" : "ופוריאון",
    "זעידן" : "ג'ולטיאון",
    "נורידן" : "פלייריאון",
    "מצולען" : "פוריגון",
    "סילוני" : "אומנייט",
    "סילוכב" : "אומסטאר",
    "פרסדה" : "קאבוטו",
    "פרצודה" : "קאבוטופס",
    "אווירונעף" : "אירודקטייל",
    "שמנמנם" : "סנורלקס",
    "קיפאוואחד" : "ארטיקונו",
    "חשמתנין" : "זאפדוס",
    "מותלאתה" : "מולטרס",
    "לטנה" : "דרטיני",
    "לטאוויר" : "דרגונייר",
    "לטאביר" : "דרגונייט",
    "תשני" : "מיוטו",
    "תש" : "מיו",
    "איריס" : "אריקה",
    "אלפרון" : "ג'ובאני",
    "איתן" : "ברונו",
    "צור" : "ברוק",
    "טל" : "מיסטי",
    "סרן ברק" : "סגן סרג'",
    "איריס" : "אריקה",
    "צפע" : "קוגה",
    "להב" : "בליין",
    "קסם" : "סברינה",
    "אירנה" : "לורליי",
    "רוחמה" : "אגתה",
    "אברי" : "לאנס",
    "הדר" : "ביל",
    "דרדר" : "פוג'י",
    "עיר הטורקיז" : "העיר סרוליאן",
    "הטורקיז" : "סרוליאן",
    "אי הצנובר" : "האי סינאבאר",
    "הצנובר" : "סינאבאר",
    "עיר הברקת" : "העיר ורידיאן",
    "הברקת" : "ורידיאן"
}
LETTER_DICTIONARY =\
{
    "א" : "E",
    "ב" : "F",
    "ג" : "G",
    "ד" : "H",
    "ה" : "I",
    "ו" : "J",
    "ז" : "K",
    "ח" : "L",
    "ט" : "M",
    "י" : "N",
    "כ" : "O",
    "ל" : "P",
    "מ" : "Q",
    "נ" : "R",
    "ס" : "S",
    "ע" : "T",
    "פ" : "U",
    "צ" : "V",
    "ק" : "W",
    "ר" : "X",
    "ש" : "Y",
    "ת" : "Z",
    "ן" : "a",
    "ם" : "b",
    "ץ" : "c",
    "ף" : "d",
    "ך" : "e",
    "<" : "{",
    ">" : "}"
}


def encode_hebrew(text, encode=True):
    for word in WORD_SWITCH_DICT:
        text = re.sub(word, WORD_SWITCH_DICT[word], text)
    if encode:
        for letter in LETTER_DICTIONARY:
            if letter in text:
                text = text.replace(letter, LETTER_DICTIONARY[letter])
    return text


def format_paragraphs(hebrew_raw_paragraphs, final_paragraphs_titels, encode=True):
    fomated_hebrew_paragraphs = []
    for lines, title in zip(hebrew_raw_paragraphs, final_paragraphs_titels):
        #lines = paragraph.splitlines()
        lines = list(filter(None, lines))
        formated_paragraph = [title]
        for line in lines:
            if re.search(INNER_TEXT_REGEX, line):
                inner_text = re.search(INNER_TEXT_REGEX, line).group(1)
                inner_text = encode_hebrew(inner_text, encode)
            else:
                inner_text = ""
            end_char = ""
            if lines.index(line) + 1 != len(lines):
                next_line = lines[lines.index(line)+1]
                if "line" in next_line:
                    end_char = r"\n"
                elif "para" in next_line:
                    end_char = r"\p"
                elif "cont" in next_line:
                    end_char = r"\l"
                if "done" in next_line or "text_end" in next_line:
                    end_char += "$"
                if "prompt" in next_line:
                    end_char += r"\p$"
            if inner_text:
                if (r"\p" not in formated_paragraph[-1]) and (((len(formated_paragraph[-1])) + len(inner_text)) < 49) and len(formated_paragraph) > 2:
                    inner_text = previus_inner_text + " " + inner_text
                    formated_paragraph[-1] = LINE_FORAMT.format(inner_text, end_char)
                else:
                    formated_paragraph.append(LINE_FORAMT.format(inner_text, end_char))
                previus_inner_text = inner_text
        fomated_hebrew_paragraphs.append("\n".join(formated_paragraph))
    return fomated_hebrew_paragraphs
        
    
def main():
    manual = False
    if len(sys.argv) < 3:
        if not (len(sys.argv) == 2 and sys.argv[1] != "maunal"):
            print(f"Usage: {sys.argv[0]} manual | <source file> <heb file> [output file] [hebrew debug file]")
            exit()
        else:
            manual = True
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = sys.argv[1].replace(".", "_reformated.")

    if not manual:
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            heb_file_data = f.read()
    else:
        heb_file_data = ""
        curr_data = None
        print("Enter heb data, enter q to finish:")
        while curr_data != "q":
            curr_data = input(">")
            heb_file_data += curr_data + "\n"
            

    hebrew_raw_paragraphs = re.findall(HEB_REGEX, heb_file_data, re.DOTALL)
    final_paragraphs_titels = [i.splitlines()[0] for i in hebrew_raw_paragraphs]
    hebrew_raw_paragraphs = [i.splitlines()[1:] for i in hebrew_raw_paragraphs]

    fomated_hebrew_paragraphs = format_paragraphs(hebrew_raw_paragraphs, final_paragraphs_titels, encode=False)

    if not manual:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(fomated_hebrew_paragraphs))

        print(f"Translation wrriten to: {output_file}")

    else:
        for par in fomated_hebrew_paragraphs:
            print(par+"\n")


if __name__ == "__main__":
    main()
