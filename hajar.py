"""
Hajar Programming Language
Version : 0.1.0-alpha
Author  : Abdullah Mohammed Bamatraf
License : MIT
GitHub  : (https://github.com/Pariq47/Hajar)
"""

VERSION = "0.1.0-alpha"
import sys


def main():
    # رسالة ترحيب عند تشغيل حجر
    print("مرحبا بك في لغة البرمجة (حجر)")
    print("Welcome to Hajar Programming Language")

    # إذا كتب المستخدم اسم ملف بعد hajar.py
    # مثل:
    # python hajar.py hello.hjr
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        run_file(filename)

    # إذا لم يكتب ملف ندخل إلى وضع REPL
    # حيث يمكن للمستخدم كتابة الأوامر مباشرة
    else:
        start_repl()


def start_repl():
    print("اكتب الكود (اكتب exit للخروج او help للمساعدة)")

    # حلقة لا نهائية حتى يكتب المستخدم exit
    while True:

        # قراءة سطر من المستخدم
        code = read_code()

        # إنهاء البرنامج
        if code == "exit":
            print("Goodbye!")
            print('وداعا!')
            break
        elif code == "help":
        	print('You can print by type "show ("<your text here>")"')
        	print('You can add a comment by type "#" before line')
        	continue

        # تجاهل السطر الفارغ
        if code.strip() == "":
            continue

        # إرسال الكود إلى المفسر
        run(code)


def read_code():
    # إظهار >>> وانتظار إدخال المستخدم
    return input(">>> ")


def run_file(filename):
    try:
        # فتح ملف حجر للقراءة
        with open(filename, "r", encoding="utf-8") as file:

            # قراءة الملف كاملاً كنص
            code = file.read()

        # إرسال محتوى الملف إلى المفسر
        run(code)

    except FileNotFoundError:
        print("error: file not found")


def run(code):
    # تقسيم الكود إلى أسطر
    lines = code.splitlines()

    # المرور على كل سطر
    for line in lines:

        # حذف المسافات من البداية والنهاية
        line = line.strip()

        # تجاهل السطور الفارغة
        if line == "":
            continue

        # تجاهل التعليقات
        # مثال:
        # # هذا تعليق
        if line.startswith("#"):
            continue

        # تنفيذ أمر show
        if line.startswith("show(") or line.startswith("show ("):
            execute_show(line)

        # إذا لم يتعرف المفسر على الأمر
        else:
            print("unknown command:", line)


def execute_show(code):
    # تقسيم السطر عند علامة الاقتباس "
    # مثال:
    # show("hello")
    # تصبح:
    # ['show(', 'hello', ')']
    parts = code.split('"')

    # التأكد من وجود نص بين علامتي الاقتباس
    if len(parts) >= 3:
        print(parts[1])

    else:
        print('error: show needs text inside ""')


# بداية تشغيل اللغة
main()
