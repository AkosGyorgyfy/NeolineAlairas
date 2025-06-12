import streamlit as st
import base64
from io import BytesIO

# Oldal konfiguráció
st.set_page_config(
    page_title="ContiBus Email Aláírás Generátor",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS stílusok
def load_css():
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #B8860B;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .template-preview {
        border: 2px solid #B8860B;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        background: linear-gradient(135deg, #f9f9f9 0%, #ffffff 100%);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .signature-output {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        background: white;
        margin: 10px 0;
        font-family: Arial, Helvetica, sans-serif;
    }
    
    .export-section {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(135deg, #B8860B 0%, #DAA520 100%);
        color: white;
    }
    
    .info-box {
        background: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #B8860B;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# ContiBus logó base64 kódolása (a feltöltött kép alapján)
def get_logo_base64():
    # Itt a logó base64 kódja lesz - jelenleg placeholder
    return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="

# Template HTML generátorok
def generate_minimalist_signature(data):
    logo_base64 = get_logo_base64()
    return f"""
    <table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, sans-serif; font-size: 14px; color: #333;">
        <tr>
            <td style="padding-right: 20px; vertical-align: top;">
                <img src="{logo_base64}" alt="ContiBus Logo" style="width: 80px; height: auto;">
            </td>
            <td style="vertical-align: top;">
                <div style="font-weight: bold; font-size: 16px; color: #B8860B; margin-bottom: 5px;">
                    {data['name']}
                </div>
                <div style="color: #666; margin-bottom: 3px;">{data['position']}</div>
                <div style="margin-bottom: 3px;">
                    <strong>Email:</strong> <a href="mailto:{data['email']}" style="color: #B8860B; text-decoration: none;">{data['email']}</a>
                </div>
                {f'<div style="margin-bottom: 3px;"><strong>Telefon:</strong> {data["phone"]}</div>' if data['phone'] else ''}
                {f'<div style="margin-bottom: 3px;"><strong>Mobil:</strong> {data["mobile"]}</div>' if data['mobile'] else ''}
                <div style="margin-top: 10px; color: #B8860B; font-weight: bold;">
                    ContiBus NEOLINE Kft.
                </div>
            </td>
        </tr>
    </table>
    """

def generate_modern_signature(data):
    logo_base64 = get_logo_base64()
    return f"""
    <table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, sans-serif; max-width: 400px;">
        <tr>
            <td style="background: linear-gradient(135deg, #B8860B 0%, #DAA520 100%); padding: 15px; border-radius: 8px 8px 0 0;">
                <div style="color: white; font-size: 18px; font-weight: bold; text-align: center;">
                    ContiBus NEOLINE Kft.
                </div>
            </td>
        </tr>
        <tr>
            <td style="background: #f9f9f9; padding: 20px; border: 1px solid #ddd; border-top: none; border-radius: 0 0 8px 8px;">
                <table cellpadding="0" cellspacing="0" border="0" width="100%">
                    <tr>
                        <td style="padding-right: 15px; vertical-align: top;">
                            <img src="{logo_base64}" alt="ContiBus Logo" style="width: 60px; height: auto;">
                        </td>
                        <td style="vertical-align: top;">
                            <div style="font-weight: bold; font-size: 16px; color: #B8860B; margin-bottom: 5px;">
                                {data['name']}
                            </div>
                            <div style="color: #666; font-style: italic; margin-bottom: 8px;">{data['position']}</div>
                            <div style="margin-bottom: 5px;">
                                📧 <a href="mailto:{data['email']}" style="color: #B8860B; text-decoration: none;">{data['email']}</a>
                            </div>
                            {f'<div style="margin-bottom: 5px;">📞 {data["phone"]}</div>' if data['phone'] else ''}
                            {f'<div style="margin-bottom: 5px;">📱 {data["mobile"]}</div>' if data['mobile'] else ''}
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    """

def generate_premium_signature(data):
    logo_base64 = get_logo_base64()
    return f"""
    <table cellpadding="0" cellspacing="0" border="0" style="font-family: 'Georgia', serif; max-width: 450px; border: 2px solid #B8860B; border-radius: 10px;">
        <tr>
            <td style="background: linear-gradient(135deg, #B8860B 0%, #DAA520 50%, #FFD700 100%); padding: 20px; text-align: center; border-radius: 8px 8px 0 0;">
                <img src="{logo_base64}" alt="ContiBus Logo" style="width: 100px; height: auto; margin-bottom: 10px;">
                <div style="color: white; font-size: 20px; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                    ContiBus NEOLINE Kft.
                </div>
                <div style="color: #fff; font-size: 14px; margin-top: 5px;">
                    Kalandozás • Utazás • Élmények
                </div>
            </td>
        </tr>
        <tr>
            <td style="padding: 25px; background: white;">
                <div style="text-align: center; margin-bottom: 20px;">
                    <div style="font-size: 18px; font-weight: bold; color: #B8860B; margin-bottom: 5px;">
                        {data['name']}
                    </div>
                    <div style="color: #666; font-size: 14px; font-style: italic;">
                        {data['position']}
                    </div>
                </div>
                <div style="border-top: 1px solid #eee; padding-top: 15px;">
                    <div style="margin-bottom: 8px;">
                        <strong style="color: #B8860B;">Email:</strong> 
                        <a href="mailto:{data['email']}" style="color: #333; text-decoration: none;">{data['email']}</a>
                    </div>
                    {f'<div style="margin-bottom: 8px;"><strong style="color: #B8860B;">Telefon:</strong> {data["phone"]}</div>' if data['phone'] else ''}
                    {f'<div style="margin-bottom: 8px;"><strong style="color: #B8860B;">Mobil:</strong> {data["mobile"]}</div>' if data['mobile'] else ''}
                </div>
                <div style="text-align: center; margin-top: 20px;">
                    <a href="#" style="background: #B8860B; color: white; padding: 8px 16px; text-decoration: none; border-radius: 20px; font-size: 12px;">
                        Kérjen Ajánlatot!
                    </a>
                </div>
            </td>
        </tr>
    </table>
    """

def generate_compact_signature(data):
    return f"""
    <div style="font-family: Arial, sans-serif; font-size: 12px; color: #333; border-top: 2px solid #B8860B; padding-top: 8px;">
        <strong style="color: #B8860B;">{data['name']}</strong> | {data['position']} | 
        <a href="mailto:{data['email']}" style="color: #B8860B; text-decoration: none;">{data['email']}</a>
        {f' | Tel: {data["phone"]}' if data['phone'] else ''}
        {f' | Mobil: {data["mobile"]}' if data['mobile'] else ''} | 
        <strong style="color: #B8860B;">ContiBus NEOLINE Kft.</strong>
    </div>
    """

# Főalkalmazás
def main():
    load_css()
    
    # Főcím
    st.markdown('<h1 class="main-header">🚌 ContiBus Email Aláírás Generátor</h1>', unsafe_allow_html=True)
    
    # Sidebar form
    with st.sidebar:
        st.header("📝 Személyes Adatok")
        
        with st.form("signature_form"):
            name = st.text_input("Név*", placeholder="Kovács János")
            position = st.text_input("Beosztás*", placeholder="Értékesítési Vezető")
            email = st.text_input("Email cím*", placeholder="kovacs.janos@contibus.hu")
            phone = st.text_input("Telefonszám", placeholder="+36 1 234 5678")
            mobile = st.text_input("Mobilszám", placeholder="+36 30 123 4567")
            
            st.markdown("---")
            template_choice = st.selectbox(
                "🎨 Template Választás",
                ["Minimalist", "Modern", "Premium", "Compact"],
                help="Válassz egy stílust az email aláírásodhoz"
            )
            
            generate_btn = st.form_submit_button("🎯 Aláírás Generálása", use_container_width=True)
    
    # Főterület
    if generate_btn and name and position and email:
        data = {
            'name': name,
            'position': position,
            'email': email,
            'phone': phone,
            'mobile': mobile
        }
        
        # Template generálás
        templates = {
            'Minimalist': generate_minimalist_signature(data),
            'Modern': generate_modern_signature(data),
            'Premium': generate_premium_signature(data),
            'Compact': generate_compact_signature(data)
        }
        
        signature_html = templates[template_choice]
        
        # Előnézet
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader(f"📧 {template_choice} Template Előnézet")
            st.markdown('<div class="signature-output">', unsafe_allow_html=True)
            st.markdown(signature_html, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
            st.markdown("**💡 Használati Útmutató:**")
            st.markdown("1. Másold ki a HTML kódot")
            st.markdown("2. Gmail/Outlook-ban illesd be")
            st.markdown("3. Állítsd be alapértelmezettként")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Exportálási opciók
        st.markdown('<div class="export-section">', unsafe_allow_html=True)
        st.subheader("📋 Exportálás")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.text_area(
                "HTML Kód (Gmail-hez):",
                signature_html,
                height=200,
                help="Másold ki ezt a kódot és illeszd be Gmail aláírás beállításaiba"
            )
        
        with col4:
            # Outlook verzió (egyszerűsített)
            outlook_html = signature_html.replace('linear-gradient(135deg, #B8860B 0%, #DAA520 100%)', '#B8860B')
            st.text_area(
                "HTML Kód (Outlook-hoz):",
                outlook_html,
                height=200,
                help="Outlook kompatibilis verzió"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Letöltési opció
        st.download_button(
            label="💾 HTML Fájl Letöltése",
            data=signature_html,
            file_name=f"contibus_signature_{template_choice.lower()}.html",
            mime="text/html"
        )
        
    elif generate_btn:
        st.error("❌ Kérlek töltsd ki a kötelező mezőket (Név, Beosztás, Email)!")
    
    else:
        # Kezdő oldal
        st.markdown("""
        ### 🌟 Üdvözlünk a ContiBus Email Aláírás Generátorban!
        
        Ez az alkalmazás segít professzionális email aláírásokat készíteni a ContiBus NEOLINE Kft. 
        márkaidentitásának megfelelően.
        
        **🚀 Funkciók:**
        - 4 különböző template stílus
        - Mobil-optimalizált design
        - Gmail és Outlook kompatibilitás
        - Azonnali előnézet
        - HTML export lehetőség
        
        **📋 Használat:**
        1. Töltsd ki a bal oldali formot a személyes adataiddal
        2. Válassz egy template stílust
        3. Kattints a "Generálás" gombra
        4. Másold ki és használd az email kliensedben
        
        *Kezdéshez töltsd ki a bal oldali formot!*
        """)
        
        # Template előnézetek
        st.subheader("🎨 Elérhető Template Stílusok")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Minimalist** - Tiszta, egyszerű")
            st.markdown("**Premium** - Teljes körű design")
        
        with col2:
            st.markdown("**Modern** - Strukturált, színes")
            st.markdown("**Compact** - Tömör, egysoros")

if __name__ == "__main__":
    main()
