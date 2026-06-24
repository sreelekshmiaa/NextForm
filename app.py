import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="NextForm♻️",
    page_icon=os.path.join(BASE_DIR, "recycle.png"),
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600;700;800&display=swap');

.stApp {
    font-family: 'Inter', sans-serif;
    background:
        linear-gradient(rgba(9, 38, 23, 0.78), rgba(190, 230, 195, 0.30)),
        url("https://images.pexels.com/photos/3013440/pexels-photo-3013440.jpeg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #f7fff7;
}

.block-container {
    padding-top: 28px;
    max-width: 1280px;
}

.hero {
    background: linear-gradient(135deg, rgba(255,255,255,0.20), rgba(255,255,255,0.08));
    padding: 55px 45px;
    border-radius: 34px;
    backdrop-filter: blur(22px);
    border: 1px solid rgba(255,255,255,0.32);
    box-shadow: 0 25px 60px rgba(0,0,0,0.30);
    min-height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.brand {
    font-family: 'Playfair Display', serif;
    font-size: 72px;
    color: #f4fff3;
    line-height: 1;
}

.tagline {
    font-size: 25px;
    color: #dff6e5;
    font-weight: 800;
    margin-top: 22px;
}

.quote {
    font-size: 18px;
    color: #edfcef;
    margin-top: 20px;
    font-style: italic;
}

.result-box {
    background: rgba(255,255,255,0.18);
    padding: 24px;
    border-radius: 24px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.25);
    margin-top: 16px;
}

.idea-card {
    background: rgba(255,255,255,0.18);
    color: #ffffff !important;
    padding: 18px 22px;
    border-radius: 18px;
    margin: 12px 0;
    border: 1px solid rgba(255,255,255,0.25);
    backdrop-filter: blur(10px);
    font-weight: 700;
}

h1, h2, h3, p, label {
    color: #f7fff7 !important;
}

.stTextInput input {
    background: rgba(200,255,220,0.25) !important;
    color: white !important;
    border: 2px solid rgba(255,255,255,0.35) !important;
    border-radius: 20px !important;
    padding: 15px !important;
}

[data-testid="stFileUploader"] {
    background: #ffd6e7 !important;
    border: 2px solid #ff8fab !important;
    border-radius: 22px !important;
    padding: 20px !important;
}

[data-testid="stFileUploaderDropzone"] {
    background: #ffe5ec !important;
    border: 2px dashed #ff8fab !important;
    border-radius: 18px !important;
}

[data-testid="stFileUploaderDropzone"] * {
    color: #ff4d8d !important;
    font-weight: 700 !important;
}

[data-testid="stFileUploaderDropzone"] button {
    background-color: #ffb3c6 !important;
    color: #5a1028 !important;
    border: 1px solid #ff8fab !important;
    border-radius: 12px !important;
    font-weight: 800 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #d8f3dc, #95d5b2);
    color: #18392b;
    border-radius: 35px;
    border: none;
    padding: 14px 30px;
    font-weight: 800;
    font-size: 17px;
}
</style>
""", unsafe_allow_html=True)


# HERO
hero_left, hero_right = st.columns([2, 4], gap="small")

with hero_left:
    greenlove_path = os.path.join(BASE_DIR, "greenlove.png")
    if os.path.exists(greenlove_path):
        st.image(greenlove_path, width=380)

with hero_right:
    st.markdown("""
    <div class="hero">
        <div class="brand">NextForm</div>
        <div class="tagline">Waste Transformation & Opportunity Platform</div>
        <div class="quote">"Every discarded object holds the potential to take on a new form."</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")


left, right = st.columns([1, 1], gap="large")

with left:
    with st.container(border=True):
        st.subheader("🌱 Start Your Transformation")

        item_name = st.text_input(
            "Enter discarded item name",
            placeholder="Example: old glass jar, plastic bottle, old t-shirt"
        )

        uploaded_image = st.file_uploader(
            "Upload image of discarded item",
            type=["jpg", "jpeg", "png"]
        )

        st.info("Small reuse ideas can create real environmental impact.")

with right:
    with st.container(border=True):
        st.subheader("⚙️ How It Works")

        st.write("""
        1. Enter or upload a discarded item.  
        2. NextForm identifies the material type.  
        3. It suggests useful upcycled product ideas.  
        4. It estimates cost, selling price, and profit.  
        5. It shows sustainability impact and SDG alignment.
        """)

        st.write("NextForm supports reuse, circular economy thinking, and responsible consumption.")

st.write("")


def analyze_with_ai(item):
    item = item.lower()

    categories = {
        "Glass": ["glass", "jar", "mirror", "glass container", "glass cup", "glass vase"],
        "Plastic": ["plastic", "bottle", "container", "packet", "wrapper", "plastic bag", "bucket", "toy", "pipe", "plastic cup", "plastic box"],
        "Fabric": ["shirt", "tshirt", "dress", "jeans", "saree", "kurti", "cloth", "clothes", "fabric", "jacket", "socks", "blanket", "curtain", "pillow cover", "bag", "uniform"],
        "Paper": ["paper", "newspaper", "magazine", "book", "notebook", "card", "paper bag"],
        "Cardboard": ["box", "cardboard", "carton", "packaging box", "delivery box", "shoe box"],
        "Metal": ["can", "tin", "steel", "iron", "metal", "aluminium", "utensil", "spoon", "fork", "pan", "pot"],
        "Wood": ["wood", "chair", "table", "furniture", "wooden box", "wood plank", "door"],
        "Electronics": ["phone", "mobile", "laptop", "computer", "keyboard", "mouse", "charger", "cable", "headphone", "television", "tv", "monitor"],
        "Rubber": ["tyre", "tire", "rubber", "tube", "slipper", "shoe"],
        "Organic": ["fruit peel", "banana peel", "vegetable waste", "food waste", "leaves", "grass", "flower", "coconut shell"]
    }

    for material, words in categories.items():
        if any(word in item for word in words):
            return material

    return "Mixed / Unknown"


def get_item_ideas(item):
    item = item.lower()

    idea_bank = {
        "bottle": ["Self-Watering Planter", "Bird Feeder", "Vertical Garden Pot", "Drip Irrigation Bottle", "Decorative Lamp"],
        "plastic bottle": ["Self-Watering Planter", "Bird Feeder", "Vertical Garden Pot", "Drip Irrigation Bottle", "Decorative Lamp"],
        "dress": ["Cushion Cover", "Patchwork Quilt", "Hair Scrunchies", "Reusable Gift Wrap", "Apron", "Pet Bed"],
        "jeans": ["Denim Tote Bag", "Pencil Pouch", "Wall Pocket Organizer", "Coasters", "Patchwork Mat"],
        "shirt": ["Tote Bag", "Cleaning Cloth", "Patchwork Pouch", "Pillow Cover", "Apron"],
        "tshirt": ["Tote Bag", "Cleaning Cloth", "Patchwork Pouch", "Pillow Cover", "Apron"],
        "jar": ["Candle Holder", "Mini Terrarium", "Spice Storage Jar", "Fairy Light Lamp", "Plant Pot"],
        "box": ["Desk Organizer", "Cat House", "Mini Bookshelf", "Seedling Tray", "Storage Drawer"],
        "newspaper": ["Paper Bags", "Gift Wrapping", "Seedling Pots", "Wall Art", "Basket Weaving"],
        "can": ["Pen Stand", "Mini Planter", "Lantern", "Kitchen Holder", "Wind Chime"],
        "phone": ["Donate or Refurbish", "CCTV Camera", "Music Player", "Digital Photo Frame", "E-waste Recycling"],
        "shoe": ["Garden Planter", "Decorative Pot", "Bird Nest Holder", "Art Piece", "Storage Holder"],
        "coconut shell": ["Bird Feeder", "Candle Bowl", "Mini Planter", "Soap Dish", "Decorative Bowl"],
        "wood": ["Wall Shelf", "Rustic Sign Board", "Plant Stand", "Photo Frame", "Mini Table"],
        "paper": ["Paper Bags", "Gift Wrapping", "Seedling Pots", "Wall Art", "Paper Pen"],
        "glass": ["Candle Holder", "Mini Terrarium", "Spice Storage Jar", "Fairy Light Lamp", "Plant Pot"]
    }

    for key, ideas in idea_bank.items():
        if key in item:
            return ideas

    return ["Creative Decor Item", "Reusable Storage Product", "Eco-Friendly Craft", "Donation or Refurbishment", "Recycling Project"]


def get_business_data(material):
    data = {
        "Glass": ("₹50 - ₹100", "₹180 - ₹300", "₹100 - ₹200", "Reduces glass waste and promotes reuse of household containers.", 95, 82, 96),
        "Plastic": ("₹20 - ₹60", "₹80 - ₹180", "₹50 - ₹120", "Prevents plastic waste from entering landfills and supports reuse.", 90, 78, 92),
        "Fabric": ("₹30 - ₹80", "₹120 - ₹280", "₹80 - ₹200", "Extends the life of fabric and reduces textile waste.", 88, 80, 90),
        "Cardboard": ("₹20 - ₹60", "₹100 - ₹200", "₹60 - ₹140", "Reduces paper waste and encourages creative reuse.", 85, 75, 88),
        "Paper": ("₹10 - ₹40", "₹50 - ₹150", "₹40 - ₹100", "Supports paper reuse and reduces demand for fresh paper products.", 84, 70, 86),
        "Metal": ("₹40 - ₹100", "₹150 - ₹350", "₹100 - ₹250", "Encourages reuse of durable metal waste and reduces scrap disposal.", 87, 82, 89),
        "Wood": ("₹50 - ₹150", "₹200 - ₹500", "₹120 - ₹350", "Promotes reuse of wood and reduces furniture waste.", 86, 85, 88),
        "Electronics": ("₹100 - ₹400", "₹300 - ₹1000", "₹150 - ₹600", "Promotes safe e-waste handling, repair, reuse, and recycling.", 78, 84, 82),
        "Rubber": ("₹40 - ₹120", "₹150 - ₹400", "₹100 - ₹280", "Reduces rubber waste and supports durable reuse products.", 82, 78, 84),
        "Organic": ("₹0 - ₹30", "₹40 - ₹120", "₹30 - ₹90", "Converts organic waste into compost or nature-friendly products.", 92, 65, 95),
        "Mixed / Unknown": ("₹30 - ₹80", "₹100 - ₹220", "₹60 - ₹150", "Encourages reuse before disposal and supports responsible consumption.", 80, 70, 85)
    }

    return data.get(material, data["Mixed / Unknown"])


if st.button("Analyze Item", use_container_width=True):

    if item_name or uploaded_image:
        item = item_name.lower() if item_name else "uploaded item"

        material = analyze_with_ai(item)
        ideas = get_item_ideas(item)
        best_form = ideas[0]

        cost, price, profit, impact, reuse_score, profit_score, sustain_score = get_business_data(material)
        overall_score = round((reuse_score + profit_score + sustain_score) / 3)

        st.success("✅ Analysis Complete!")
        st.header("NextForm Analysis")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Reusability", f"{reuse_score}/100")
        c2.metric("Profitability", f"{profit_score}/100")
        c3.metric("Sustainability", f"{sustain_score}/100")
        c4.metric("NextForm Score", f"{overall_score}/100")

        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("🔍 Item Understanding")
            st.markdown(f"### 🔍 Detected Material: **{material}**")
            st.markdown(f"### ✨ Best Next Form: **{best_form}**")
            st.markdown('</div>', unsafe_allow_html=True)

            st.subheader("💡 Suggested Next Forms")
            for idea in ideas:
                st.markdown(f'<div class="idea-card">♻️ {idea}</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("💰 Business Opportunity")
            st.write("**Estimated Making Cost:**", cost)
            st.write("**Estimated Selling Price:**", price)
            st.write("**Estimated Profit:**", profit)

            st.subheader("🌍 Sustainability Impact")
            st.write(impact)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("🎯 SDG Alignment")
        st.write("**Primary SDG:** SDG 12 – Responsible Consumption and Production")
        st.write("NextForm supports reuse, upcycling, and circular economy practices.")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("🤝 Responsible Use Notice")
        st.write("""
        • No API key is required  
        • No user data is stored  
        • Suggestions are basic reuse ideas  
        • Business estimates should be verified with local market research  
        • This project supports responsible consumption and sustainability  
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("Please enter an item name or upload an image.")


