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
    return "image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="

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
                     NEOLINE Kft.
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
                        Kérjen Ajánlat
