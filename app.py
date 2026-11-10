import re
import streamlit as st
from supabase import create_client

# ======================================
# 1. PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="GreenHarvest Agriculture",
    page_icon="🌱",
    layout="wide"
)

# ======================================
# 2. NAVIGATION FUNCTION
# ======================================

def navigate_to(page_name):
    st.session_state.page = page_name


if "page" not in st.session_state:
    st.session_state.page = "Home"

# ======================================
# 3. CUSTOM CSS
# ======================================

st.markdown("""
<style>
.stApp {
    background-color: #f7faf5;
}

h1, h2, h3 {
    color: #174d32;
}

/* Hero Section */
.hero {
    background-image:
        linear-gradient(
            rgba(15, 45, 25, 0.55),
            rgba(15, 45, 25, 0.55)
        ),
        url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1600");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    padding: 90px 35px;
    border-radius: 18px;
    min-height: 350px;
    text-align: center;
}

.hero h1,
.hero p {
    color: white !important;
}

/* Buttons */
div.stButton > button {
    background-color: #e8b83f;
    color: #174d32;
    border-radius: 8px;
    border: none;
    font-weight: bold;
    padding: 10px;
}

div.stButton > button:hover {
    background-color: #d4a72e;
    color: #174d32;
}

/* Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 12px;
}

/* Responsive Hero */
@media (max-width: 768px) {
    .hero {
        padding: 55px 15px;
        min-height: 300px;
    }

    .hero h1 {
        font-size: 32px !important;
    }

    .hero p {
        font-size: 16px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ======================================
# 4. SIDEBAR NAVIGATION
# ======================================

st.sidebar.title("🌱 GreenHarvest")
st.sidebar.write("Smarter Farming, Greener Future")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "About Us",
        "Products & Services",
        "Farming Solutions",
        "Contact",
        "AI Assistant"
    ],
    key="page"
)

# ======================================
# 5. HOME PAGE
# ======================================

if page == "Home":

   # 5.1 HERO SECTION

    st.markdown("""
    <div class="hero">
        <p style="font-size: 14px; letter-spacing: 3px; font-weight: bold;">
            SUSTAINABLE AGRICULTURE • SMARTER FARMING
        </p>
        <h1>Growing a Greener Tomorrow</h1>
        <p>
            Empowering farmers with innovative technology,
            sustainable farming practices and smarter agricultural solutions
            for a healthier and more productive future.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 5.2 CALL TO ACTION BUTTONS
    st.write("")
    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        st.button(
            "Explore Our Solutions",
            on_click=navigate_to,
            args=("Farming Solutions",),
            use_container_width=True
        )

    with col2:
        st.button(
            "Meet Our Team",
            on_click=navigate_to,
            args=("About Us",),
            use_container_width=True
        )

    # 5.3 IMPACT STATISTICS
    st.divider()
    st.subheader("Our Growing Impact")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Farmers Supported", "5,000+")
    col2.metric("Acres Covered", "12,000+")
    col3.metric("Water Saved", "30%")
    col4.metric("Sustainable Solutions", "25+")

    # 5.4 AGRICULTURE SERVICES
    st.divider()
    st.header("Our Agriculture Services")
    st.write(
        "Supporting farmers with practical and sustainable "
        "agricultural solutions."
    )

    services = [
        (
            "🌱 Organic Farming",
            "Promoting natural farming methods and healthy crop production."
        ),
        (
            "💧 Smart Irrigation",
            "Improving water efficiency with smarter irrigation solutions."
        ),
        (
            "🌾 Quality Seeds",
            "Supporting better crop growth with quality seed selection."
        ),
        (
            "🚜 Farm Consultancy",
            "Providing expert guidance for productive farming."
        )
    ]

    col1, col2 = st.columns(2)
    for index, (name, description) in enumerate(services):
        current_col = col1 if index % 2 == 0 else col2
        with current_col:
            with st.container(border=True):
                st.subheader(name)
                st.write(description)

    # 5.5 WHY CHOOSE GREENHARVEST
    st.divider()
    st.header("Why Choose GreenHarvest?")
    st.write(
        "Helping farmers grow better through innovation and sustainability."
    )

    features = [
        (
            "🌍 Sustainable Agriculture",
            "We encourage environmentally responsible farming practices "
            "that protect natural resources."
        ),
        (
            "💧 Smart Resource Management",
            "We promote efficient water and soil management "
            "to support healthier crops."
        ),
        (
            "🚜 Modern Technology",
            "We bring modern agricultural technology and "
            "innovative solutions closer to farmers."
        ),
        (
            "🤝 Farmer-Focused Support",
            "We provide practical guidance and solutions "
            "to help farmers improve productivity."
        )
    ]

    col1, col2 = st.columns(2)
    for index, (title, description) in enumerate(features):
        current_col = col1 if index % 2 == 0 else col2
        with current_col:
            with st.container(border=True):
                st.subheader(title)
                st.write(description)

    # 5.6 FARMER TESTIMONIALS
    st.divider()
    st.header("What Farmers Say")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.write(
                "The smart irrigation solutions helped us "
                "understand how to manage water more efficiently."
            )
            st.caption("Ramesh Kumar | Farmer | Telangana")

    with col2:
        with st.container(border=True):
            st.write(
                "Their organic farming guidance gave us useful "
                "ideas for improving our farming practices."
            )
            st.caption("Suresh Patel | Farmer | Maharashtra")

    with col3:
        with st.container(border=True):
            st.write(
                "The agricultural technology solutions made "
                "farm management easier for us."
            )
            st.caption("Anita Devi | Farmer | Karnataka")

# ======================================
# 6. ABOUT US
# ======================================

elif page == "About Us":

    st.title("About GreenHarvest Agriculture")
    st.write(
        "GreenHarvest Agriculture is focused on supporting farmers "
        "through sustainable agricultural practices, modern technology "
        "and innovative farming solutions."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1500382017468-9049fed747ef",
            use_container_width=True
        )

    with col2:
        st.subheader("Growing Together")
        st.write(
            "We believe agriculture is the foundation of a sustainable "
            "future. Our goal is to help farmers adopt smarter farming "
            "methods, improve resource management and support healthier "
            "crop production."
        )

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("🎯 Our Mission")
            st.write(
                "To empower farmers with sustainable agricultural "
                "practices, innovative technology and practical "
                "farming solutions."
            )

    with col2:
        with st.container(border=True):
            st.subheader("🌍 Our Vision")
            st.write(
                "To create a greener agricultural future where "
                "technology, sustainability and farming work together."
            )

    st.divider()
    st.subheader("Our Contribution to Farmers")
    st.write(
        "We support farmers by promoting water conservation, "
        "soil health, organic farming, modern agricultural "
        "technology and practical farming guidance."
    )

# ======================================
# 7. PRODUCTS & SERVICES
# ======================================

elif page == "Products & Services":

    st.title("Our Products & Services")
    st.write(
        "Explore our agricultural products and services "
        "designed to support smarter farming."
    )

    products = [
        {
            "name": "Organic Fertilizers",
            "description": (
                "Natural fertilizers that support soil health "
                "and sustainable crop growth."
            ),
            "image": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b"
        },
        {
            "name": "Quality Seeds",
            "description": (
                "Quality seed selection to support healthy "
                "and productive crop cultivation."
            ),
            "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef"
        },
        {
            "name": "Irrigation Systems",
            "description": (
                "Efficient irrigation solutions that help "
                "farmers manage water resources."
            ),
            "image": "https://images.unsplash.com/photo-1563514227147-6d2ff665a6a0"
        },
        {
            "name": "Farm Equipment",
            "description": (
                "Modern agricultural equipment to support "
                "efficient farming operations."
            ),
            "image": "https://images.unsplash.com/photo-1592982537447-7440770cbfc9"
        }
    ]

    for row in range(0, len(products), 2):
        col1, col2 = st.columns(2)

        for col, index in zip([col1, col2], [row, row + 1]):
            if index < len(products):
                product = products[index]

                with col:
                    with st.container(border=True):
                        st.image(
                            product["image"],
                            use_container_width=True
                        )
                        st.subheader(product["name"])
                        st.write(product["description"])

                        if st.button(
                            "Learn More",
                            key=f"product_{index}",
                            use_container_width=True
                        ):
                            st.info(
                                f"More information about "
                                f"{product['name']} is coming soon."
                            )

# ======================================
# 8. FARMING SOLUTIONS
# ======================================

elif page == "Farming Solutions":

    st.title("Smart Farming Solutions")
    st.write(
        "Discover innovative solutions that help farmers "
        "improve efficiency and sustainability."
    )

    solutions = [
        (
            "🌱",
            "Smart Farming",
            "Using modern technology to improve agricultural productivity."
        ),
        (
            "💧",
            "Water Management",
            "Managing water resources efficiently through smart irrigation."
        ),
        (
            "🌍",
            "Soil Health Monitoring",
            "Supporting healthy soil through better monitoring and management."
        ),
        (
            "🛡️",
            "Crop Disease Prevention",
            "Encouraging early identification and prevention of crop diseases."
        )
    ]

    for icon, name, description in solutions:
        with st.container(border=True):
            st.subheader(f"{icon} {name}")
            st.write(description)

# ======================================
# 9. CONTACT
# ======================================


elif page == "Contact":

    st.title("Contact GreenHarvest")
    st.write(
        "Have questions about our agricultural solutions? "
        "Send us a message."
    )

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        phone = st.text_input("Phone Number")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button(
            "Submit Message",
            use_container_width=True
        )

        if submitted:
            if not name.strip() or not email.strip() or not message.strip():
                st.error("Please fill in your name, email and message.")

            elif not re.fullmatch(
                r"[^@\s]+@[^@\s]+\.[^@\s]+",
                email.strip()
            ):
                st.error("Please enter a valid email address.")

            else:
                try:
                    supabase = create_client(
                        st.secrets["SUPABASE_URL"],
                        st.secrets["SUPABASE_KEY"]
                    )

                    response = supabase.table("enquiries").insert({
                        "name": name.strip(),
                        "email": email.strip(),
                        "phone": phone.strip(),
                        "message": message.strip()
                    }).execute()

                    if response.data:
                        st.success(
                            f"Thank you, {name}! "
                            "Your enquiry has been saved successfully."
                        )
                    else:
                        st.error("Unable to save your enquiry.")

                except Exception as e:
                    st.error(f"Database error: {e}")

    st.divider()
    st.subheader("Business Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("📧 Email: arif@greenharvest.com")
        st.write("📞 Phone: +917674025108")

    with col2:
        st.write("📍 Location: pedana, India")


# ======================================
# 10. AI ASSISTANT
# ======================================

elif page == "AI Assistant":

    st.title("🌱 GreenHarvest AI Assistant")
    st.write(
        "Your smart farming assistant. Ask questions about crops, "
        "soil health, irrigation, fertilizers and sustainable agriculture."
    )
    st.info(
        "AI chatbot integration is coming soon. "
        "We will connect an agriculture-focused AI assistant here."
    )

# ======================================
# 11. FOOTER
# ======================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🌱 GreenHarvest Agriculture")
    st.write(
        "Growing a greener future through sustainable agriculture "
        "and smarter farming solutions."
    )

with col2:
    st.subheader("Quick Navigation")
    st.button(
        "Home",
        key="footer_home",
        on_click=navigate_to,
        args=("Home",)
    )
    st.button(
        "About Us",
        key="footer_about",
        on_click=navigate_to,
        args=("About Us",)
    )
    st.button(
        "Contact",
        key="footer_contact",
        on_click=navigate_to,
        args=("Contact",)
    )

with col3:
    st.subheader("Contact Information")
    st.write("📧 arif@greenharvest.com")
    st.write("📞 +91 7674025108")
    st.write("📍 Pedana, Andhra Pradesh, India")

st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>© 2026 GreenHarvest Agriculture. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
