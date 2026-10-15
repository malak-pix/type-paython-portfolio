#session_timer
# Convert a session length in seconds to minutes and seconds.
total_seconed = int(input("session length in seconds is:"))#هون بدخل القيمة المستخدم بعدين بيحولها من نص ل رقم صحيح وبيخزنها ب المتغير
minutes = total_seconed//60
sec = total_seconed % 60
print(f"Session Length:{minutes} minutes and {sec} seconds")
#لما ندخل 905 اعطاني 15 دقيقة و5 ثوان
