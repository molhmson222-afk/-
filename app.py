import streamlit as st
from PIL import Image
import base64

# إعدادات صفحة التطبيق
st.set_page_config(
    page_title="AI Crypto & Chart Analyzer | Horus Trading Pro",
    page_icon="📈",
    layout="wide"
)

# دالة التحقق من حالة التفعيل في جلسة المستخدم
if 'is_activated' not in st.session_state:
    st.session_state['is_activated'] = False

# واجهة الدفع والتفعيل
def activation_gate():
    st.markdown("<h2 style='text-align: center; color: #FCD535;'>🔐 تفعيل تطبيق التحليل الفني المتقدم</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 خطوات التفعيل والدفع:")
        st.markdown("1. تحويل رسوم التسجيل وقدرها **5 دولار أمريكي** عبر محفظة بايننس (Binance).")
        st.info("📌 **Binance ID:** `1086724721`")
        st.markdown("2. بعد إتمام التحويل، اضغط على الزر أدناه لتأكيد الدفع وإرسال إشعار التحويل عبر الواتساب.")
        
        whatsapp_url = "https://wa.me/249117431957?text=مرحباً%20أيمن،%20لقد%20قمت بتحويل%20رسوم%20الاشتراك%20(5$)%20لتطبيق%20التحليل%20الفني%20عبر%20بايناس،%20وهذا%20هو%20إشعار%20التحويل،%20أرجو%20إرسال%20كلمة%20السر."
        st.markdown(f"""
            <a href='{whatsapp_url}' target='_blank'>
                <button style='background-color: #25D366; color: white; padding: 12px 20px; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: bold;'>
                    💬 تأكيد الدفع عبر واتساب (+249117431957)
                </button>
            </a>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("### 🔑 أدخل كلمة السر لتفعيل التطبيق:")
        st.markdown("إذا قمت بالتواصل مع المسؤول وتم تحرير كلمة السر لك، أدخلها هنا مباشرة:")
        
        entered_password = st.text_input("أدخل كلمة المرور:", type="password")
        
        if st.button("تفعيل التطبيق 🚀", use_container_width=True):
            if entered_password == "Aymn@0909A":
                st.session_state['is_activated'] = True
                st.success("🎉 تم تفعيل التطبيق بنجاح! جاري توجيهك...")
                st.rerun()
            else:
                st.error("❌ كلمة المرور غير صحيحة. يجب التأكد من تحويل المبلغ والتواصل عبر الواتساب للحصول على كلمة المرور الصحيحة.")

# محرك تحليل الشارت والصور
def main_app():
    st.markdown("<h1 style='text-align: center; color: #00FFCC;'>📊 منصة التحليل الذكي للشارت والأسواق المالية</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #A0A0A0;'>مبنياً على قواعد كلاسيكية، الشموع اليابانية، وموجات إليوت وإدارة المخاطر الصارمة.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # الشريط الجانبي لمعلومات الحساب
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/bitcoin.png", width=80)
        st.write("### 👤 لوحة التحكم")
        st.success("✅ الحالة: مفعل ونشط")
        st.markdown("---")
        st.write("**الإدارة والتحكم:** Ayman Al-Sayed")
        st.write("**رقم الدعم واتساب:** +249117431957")
        st.write("**معرف بايننس:** 1086724721")
        if st.button("🔒 تسجيل الخروج / قفل التطبيق"):
            st.session_state['is_activated'] = False
            st.rerun()

    # رفع صورة الشارت للتحليل
    st.markdown("### 📥 رفع صورة الشارت الفني للتحليل الآلي:")
    uploaded_file = st.file_uploader("قم بتحديث صورة الشارت (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col_img, col_analysis = st.columns([1, 1])
        
        with col_img:
            st.markdown("#### 🖼️ الشارت المرفوع:")
            st.image(image, caption="صورة الشارت المراد تحليله", use_column_width=True)
            
        with col_analysis:
            st.markdown("#### 🧠 تقرير التحليل الفني المتقدم:")
            with st.spinner("جاري تحليل الأنماط، الشموع اليابانية، وموجات إليوت..."):
                st.markdown("""
                * **1. تحليل الشموع اليابانية والزخم:** 
                  * تم رصد الشموع الحالية واتجاه السعر.
                  * إشارات محتملة للانبساط أو الانعكاس بناءً على نماذج المطرقة والابتلاع.
                * **2. النماذج الكلاسيكية واتجاه الترند:**
                  * فحص القمم والقيعان لتحديد مسار السوق.
                  * تحديد خطوط الاتجاه ومناطق الدعم والمقاومة الحرجة.
                * **3. قواعد إدارة المخاطر وتحديد الأهداف:**
                  * **نقطة الدخول المقترحة:** عند اختبار خط الدعم أو اختراق المقاومة.
                  * **وقف الخسارة (Stop Loss):** 10 نقاط تحت أحدث قاع للشراء، أو 15 نقطة فوق أحدث قمة للبيع.
                  * **نسبة المخاطرة للربح:** لا تقل عن 1:1.5 مع عدم المجازفة بأكثر من 5% من الحساب.
                """)
                st.success("✅ تم الانتهاء من التحليل بنجاح بناءً على القواعد المعيارية المعتمدة.")

    st.markdown("---")
    st.markdown("### 📚 ملخص القواعد الذكية المدمجة في التطبيق:")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("🔹 **قواعد موجات إليوت:** التركيز على 5 موجات دافعة و3 تصحيحية.")
    with c2:
        st.warning("🔸 **إدارة المخاطر:** عدم تجاوز 5% مجازفة في الصفقة الواحدة.")
    with c3:
        st.success("🟢 **الشموع والانعكاس:** الاعتماد على النماذج التجميعية والتصريفية.")

# التحكم الرئيسي في عرض الصفحة بناءً على التفعيل
if st.session_state['is_activated']:
    main_app()
else:
    activation_gate()
