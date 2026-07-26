import streamlit as st



def footer_home():
    
    st.markdown("""
    <style>
    .footer-container{
        margin-top:2rem;
        display:flex;
        justify-content:center;
        align-items:center;
        gap:8px;
        flex-wrap:wrap;
        text-align:center;
    }

    .footer-text{
        font-weight:bold;
        color:white;
        margin:0;
        font-size:clamp(16px,2vw,20px);
    }

    .footer-name{
        margin:0;
        color:#ffffff;
        font-family:'Arial Black', Arial, sans-serif;
        font-size:clamp(22px,4vw,34px);
        font-weight:900;
        letter-spacing:2px;
        line-height:1;
    }

    @media (max-width:768px){
        .footer-container{
            flex-direction:column;
            gap:4px;
        }

        .footer-name{
            font-size:28px;
        }
    }
    </style>

    <div class="footer-container">
        <p class="footer-text">Created by</p>
        <p class="footer-name">SAURABH</p>
    </div>
    """, unsafe_allow_html=True)