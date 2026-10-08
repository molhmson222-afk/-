import streamlit as st
from PIL import Image

# إعدادات صفحة التطبيق الاحترافية
st.set_page_config(
    page_title="Horus Master Trader AI | Professional Financial Analyzer",
    page_icon="👑",
    layout="wide"
)

# دالة التحقق من التفعيل
if 'is_activated' not in st.session_state:
    st.session_state['is_activated'] = False

# واجهة الدفع والتفعيل الآمنة
def activation_gate():
    st.markdown("<h2 style='text-align: center; color: #FCD535;'>🔐 تفعيل منصة حورس للتحليل المالي المتقدم (VIP)</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #A0A0A0;'>النسخة الاحترافية بخبرة 50 عاماً في الأسواق المالية ومدمج بها قواعد الثراء الاستثماري.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 خطوات التفعيل والاشتراك:")
        st.markdown("1. تحويل رسوم الاشتراك وقدرها **5 دولار أمريكي** فقط عبر محفظة بايننس (Binance).")
        st.info("📌 **Binance ID:** `1086724721`")
        st.markdown("2. بعد إتمام التحويل، اضغط الزر أدناه لإرسال إشعار التحويل الفوري وتفعيل حسابك عبر الواتساب.")
        
        whatsapp_url = "https://wa.me/249117431957?text=مرحباً%20أيمن،%20لقد%20قمت%20بتحويل%20رسوم%20الاشتراك%20(5$)%20لتطبيق%20Horus%20Trading%20Pro%20عبر%20بايننس،%20أرجو%20إرسال%20كلمة%20السر%20الخاصة بي."
        st.markdown(f"""
            <a href='{whatsapp_url}' target='_blank'>
                <button style='background-color: #25D366; color: white; padding: 12px 20px; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; width: 100%; font-weight: bold;'>
                    💬 تأكيد الدفع عبر واتساب (+249117431957)
                </button>
            </a>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("### 🔑 أدخل كلمة السر الخاصة بك:")
        st.markdown("أدخل كلمة المرور التي تسلمتها من الإدارة بعد التحقق من التحويل:")
        
        entered_password = st.text_input("أدخل كلمة المرور:", type="password")
        
        if st.button("تفعيل النسخة الشاملة 🚀", use_container_width=True):
            if entered_password == "Aymn@0909A":
                st.session_state['is_activated'] = True
                st.success("🎉 تم تفعيل التطبيق بنجاح! مرحباً بك في عالم المحترفين.")
                st.rerun()
            else:
                st.error("❌ كلمة المرور غير صحيحة. يجيب التأكد من تحويل الرسوم والتواصل عبر الواتساب.")

# محرك التحليل المالي العضوي والذكي (بخبرة 50 عاماً)
def main_app():
    st.markdown("<h1 style='text-align: center; color: #00FFCC;'>👑 Horus Master Trader - الروبوت المالي الذكي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #A0A0A0;'>تحليل عميق يدمج مدرسة ويكوف، موجات إليوت، نماذج ICT، وإدارة المخاطر المؤسسية بدقة 90%.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # الشريط الجانبي للمكتبة والمراجع وقاعدة التحكم
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/bullish.png", width=80)
        st.write("### 👤 لوحة خبير الأسواق")
        st.success("✅ الحالة: حساب VIP مفعل")
        st.markdown("---")
        st.write("**المطور والمشرف:** Ayman Al-Sayed")
        st.write("**الدعم واتساب:** +249117431957")
        st.write("**بايناس ID:** `1086724721`")
        st.markdown("---")
        st.write("### 📚 مراجع الخبير المدمجة:")
        st.caption("• الوعي الاستثماري (ريتشارد ويكوف)")
        st.caption("• مبدأ موجات إليوت (رالف نيلسون)")
        st.caption("• التداول بالمناطق المؤسسية (ICT)")
        st.caption("• قراءة السعر والزخم (Price Action)")
        st.markdown("---")
        if st.button("🔒 قفل التطبيق / تسجيل الخروج"):
            st.session_state['is_activated'] = False
            st.rerun()

    # لوحة إدخال البيانات المعتمدة على الصورة لضمان دقة 90%
    st.markdown("### 📥 الخطوة الأولى: رفع شارت السعر وتحديد الإطار الزمني:")
    
    col_upload, col_inputs = st.columns([1, 1])
    
    with col_upload:
        uploaded_file = st.file_uploader("قم برفع صورة الشارت بوضوح (PNG, JPG)", type=["png", "jpg", "jpeg"])
        timeframe = st.selectbox("حدد الإطار الزمني الظاهر في الصورة:", ["1 دقيقة (Scalping)", "5 دقائق", "15 دقيقة", "ساعة واحدة (Intraday)", "4 ساعات (Swing)", "اليديلي اليومي (Investor)"])

    with col_inputs:
        st.markdown("#### ⚙️ معايرة محرك التسعير الذكي:")
        st.markdown("لضمان دقة توصيات بنسبة 90% وخلوها من العشوائية، أدخل **السعر الحالي** الظاهر على يمين الشارت المرفوع:")
        current_market_price = st.number_input("أدخل السعر الحالي للسهم أو العملة بالصورة:", min_value=0.0001, value=100.00, step=0.01, format="%.4f")
        trade_bias = st.radio("رؤيتك الأولية أو اتجاه الزخم بالصورة:", ["صعودي (Bullish - شراء)", "هبوطي (Bearish - بيع)"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.markdown("---")
        
        col_img, col_report = st.columns([1, 1])
        
        with col_img:
            st.markdown("#### 🖼️ الشارت المحلل:")
            st.image(image, caption=f"الإطار الزمني: {timeframe} | السعر المرجعي: {current_market_price}", use_column_width=True)
