import streamlit as st
import pandas as pd
import time


st.set_page_config(
    page_title="Main Dashboard",  # the page title shown in the browser tab
    page_icon="🛫",  # the page favicon shown in the browser tab
    layout="wide",  # page layout : use the entire screen
    initial_sidebar_state="expanded" 
)

st.title("OneMedia3 Operations Dashboard")

with st.sidebar:
    #st.sidebar.image(image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5NVbU9neMehpoxRiJVTCUkvayZ0LNukE39Q&s")
    st.sidebar.title('OneMedia3')
    st.page_link("pages/dashboard.py", label="Dashboard")
    st.page_link("pages/campaigns.py", label="Campaigns")
    st.page_link("login.py", label="Return to Login")
    
    
# New Campaign Button
with st.container(horizontal=True):
    st.space("stretch")
    if st.button("Create New Campaign +", type="primary"):
        st.switch_page("pages/create_campaign.py")

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4, border=True)
with col1:

    st.header("Zones Forecasted")
    st.subheader("651")
with col2:
    st.header("Active Campaigns")
    st.subheader("238")
with col3:
    st.header("Zone Allocations")
    st.subheader("10,866")
with col4:
    st.header("Alerts Fired")
    st.subheader("13")

# table @ bottom
data = {
    'Queue Item': ['Panasillies Banner Campaign', 'Panasillies Video Pre-roll', 'eXW Adload 0429'],
    'Type': ['Banner', "Video", 'Video'],
    'Status': ['On-Track', 'Under-Pacing', 'Over-Pacing'],
    'Action': ['Continue', 'Review', 'Review']
}
# df = pd.DataFrame(data)
# edited_df = st.data_editor(df)
with st.container(border=True):
    st.header('Campaigns to Review')
    st.table(data, border='horizontal')


     




# # --- Page Config ---
# st.set_page_config(
#     page_title="OneMedia3 - Panasillies",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # --- Session State Init ---
# if "page" not in st.session_state:
#     st.session_state.page = "dashboard"

# # --- Custom CSS ---
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

#     html, body, [class*="css"] {
#         font-family: 'DM Sans', sans-serif;
#     }

#     [data-testid="stSidebar"] {
#         background-color: #1a2332;
#         padding-top: 0;
#     }

#     .topbar {
#         background-color: #1a2332;
#         padding: 10px 24px;
#         display: flex;
#         align-items: center;
#         gap: 32px;
#         border-radius: 6px;
#         margin-bottom: 20px;
#     }
#     .topbar a { color: #cdd5e0; text-decoration: none; font-size: 14px; font-weight: 500; }
#     .topbar .logged-in { margin-left: auto; color: #8899aa; font-size: 12px; }

#     .stat-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px 24px; }
#     .stat-label { font-size: 14px; font-weight: 600; color: #1a2332; margin-bottom: 8px; }
#     .stat-number { font-size: 40px; font-weight: 700; color: #1a2332; line-height: 1; margin-bottom: 4px; }
#     .stat-sub { font-size: 13px; color: #94a3b8; }

#     .platform-btn {
#         display: block; width: 100%; background: white;
#         border: 1px solid #e2e8f0; border-radius: 6px;
#         padding: 10px 14px; margin-bottom: 8px;
#         font-size: 13px; color: #1a2332; font-weight: 500;
#     }

#     .queue-table { width: 100%; border-collapse: collapse; font-size: 14px; }
#     .queue-table th { text-align: left; padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #64748b; font-weight: 600; font-size: 13px; }
#     .queue-table td { padding: 12px 12px; border-bottom: 1px solid #f1f5f9; color: #1e293b; }
#     .queue-table tr:last-child td { border-bottom: none; }
#     .action-link { color: #2563eb; text-decoration: none; font-weight: 500; }

#     .stButton > button {
#         background-color: #2563eb !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 6px !important;
#         font-weight: 600 !important;
#         font-size: 14px !important;
#     }
#     .stButton > button:hover { background-color: #1d4ed8 !important; }

#     .main .block-container { background-color: #f1f5f9; padding-top: 20px; }
#     .breadcrumb { font-size: 12px; color: #94a3b8; margin-bottom: 4px; }

#     .section-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; }
#     .section-title { font-size: 15px; font-weight: 700; color: #1a2332; margin-bottom: 16px; }

#     .form-card { background: white; border: 1px solid #e2e8f0; border-radius: 8px; padding: 28px 32px; margin-bottom: 16px; }
#     .form-section-title {
#         font-size: 13px; font-weight: 700; color: #64748b;
#         text-transform: uppercase; letter-spacing: 0.05em;
#         margin-bottom: 16px; padding-bottom: 8px;
#         border-bottom: 1px solid #f1f5f9;
#     }

#     .success-banner {
#         background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px;
#         padding: 14px 20px; color: #166534; font-weight: 600;
#         margin-bottom: 20px; font-size: 14px;
#     }
# </style>
# """, unsafe_allow_html=True)


# # ── Shared Sidebar ────────────────────────────────────────────────────────
# def render_sidebar(active="Dashboard"):
#     with st.sidebar:
#         st.markdown("""
#         <div style="background:#2563eb; padding:14px 20px; margin:-1rem -1rem 16px -1rem; border-radius:0;">
#             <span style="color:white; font-weight:700; font-size:15px;">OneMedia3 - Panasillies</span>
#         </div>
#         """, unsafe_allow_html=True)

#         nav_items = [
#             "Dashboard", "Advertisers",
#             "Campaigns", "Manage Campaigns"
            
#         ]
#         # "Dashboard", "Advertisers", "Airline Programs", "Seat Classes",
#         #     "Languages", "Aircraft Types", "City Pairs", "Route Groups",
#         #     "Video Zones", "Campaigns", "Creatives", "Manage Campaigns",
#         #     "MMA", "Exports", "Reports"
#         for item in nav_items:
#             is_active = item == active
#             bg = "#2563eb" if is_active else "transparent"
#             color = "white" if is_active else "#cdd5e0"
#             weight = "700" if is_active else "400"
#             st.markdown(f"""
#             <div style="background:{bg}; color:{color}; padding:8px 16px;
#                         border-radius:4px; margin:2px 0; font-size:14px; font-weight:{weight};">
#                 {item}
#             </div>""", unsafe_allow_html=True)


# # ── Shared Topbar ─────────────────────────────────────────────────────────
# def render_topbar():
#     st.markdown("""
#     <div class="topbar">
#         <a href="#">Campaigns</a>
#         <a href="#">Profile Setup</a>
#         <a href="#">Approvals</a>
#         <a href="#">MMA</a>
#         <a href="#">Exports</a>
#         <a href="#">Reports</a>
#         <span class="logged-in">LOGGED IN AS: xxxxx</span>
#     </div>
#     """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════════════════════════════════
# # PAGE: Dashboard
# # ══════════════════════════════════════════════════════════════════════════
# def show_dashboard():
#     render_sidebar("Dashboard")
#     render_topbar()

#     st.markdown('<div class="breadcrumb">OneMedia / Dashboard</div>', unsafe_allow_html=True)

#     title_col, btn_col = st.columns([4, 1])
#     with title_col:
#         st.markdown("<h2 style='margin:0 0 20px 0; color:#1a2332; font-size:26px; font-weight:700;'>OneMedia3 Operations Dashboard</h2>", unsafe_allow_html=True)
#     with btn_col:
#         if st.button("＋ Create Campaign", use_container_width=True):
#             st.session_state.page = "create_campaign"
#             st.rerun()

#     # Stat Cards
#     c1, c2, c3, c4 = st.columns(4)
#     stats = [
#         ("Active Campaigns", "18", "Active Campaigns"),
#         ("Creatives Pending", "7", "Creatives Pending"),
#         ("Adload Ready", "4", "Adload Ready"),
#         ("Targeting Channels", "31", "Targeting Channels"),
#     ]
#     for col, (label, number, sub) in zip([c1, c2, c3, c4], stats):
#         with col:
#             st.markdown(f"""
#             <div class="stat-card">
#                 <div class="stat-label">{label}</div>
#                 <div class="stat-number">{number}</div>
#                 <div class="stat-sub">{sub}</div>
#             </div>
#             """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     left_col, right_col = st.columns([3, 1])

#     with left_col:
#         st.markdown("""
#         <div class="section-card">
#             <table class="queue-table">
#                 <thead>
#                     <tr>
#                         <th>Queue Item</th><th>Type</th><th>Status</th><th>Action</th>
#                     </tr>
#                 </thead>
#                 <tbody>
#                     <tr>
#                         <td><strong>Panasillies Banner Campaign</strong></td>
#                         <td>Banner</td><td>Open</td>
#                         <td><a class="action-link" href="#">Continue</a></td>
#                     </tr>
#                     <tr>
#                         <td><strong>Panasillies Video Pre-roll</strong></td>
#                         <td>Video</td><td>In Review</td>
#                         <td><a class="action-link" href="#">Review</a></td>
#                     </tr>
#                     <tr>
#                         <td><strong>eXW Adload 0429</strong></td>
#                         <td>Export</td><td>Ready</td>
#                         <td><a class="action-link" href="#">Inspect</a></td>
#                     </tr>
#                 </tbody>
#             </table>
#         </div>
#         """, unsafe_allow_html=True)

#     with right_col:
#         st.markdown("""
#         <div class="section-card">
#             <div class="section-title">Platform Map</div>
#             <div class="platform-btn">Profile Setup</div>
#             <div class="platform-btn">Targeting</div>
#             <div class="platform-btn">Campaigns</div>

#         </div>
#         """, unsafe_allow_html=True)

#             # <div class="platform-btn">Creatives</div>
#             # <div class="platform-btn">MMA</div>
#             # <div class="platform-btn">Exports</div>
#             # <div class="platform-btn">Reports</div>

# # ══════════════════════════════════════════════════════════════════════════
# # PAGE: Create Campaign
# # ══════════════════════════════════════════════════════════════════════════
# def show_create_campaign():
#     render_sidebar("Campaigns")
#     render_topbar()

#     st.markdown('<div class="breadcrumb">OneMedia / Dashboard / Create Campaign</div>', unsafe_allow_html=True)

#     title_col, back_col = st.columns([4, 1])
#     with title_col:
#         st.markdown("<h2 style='margin:0 0 20px 0; color:#1a2332; font-size:26px; font-weight:700;'>Create Campaign</h2>", unsafe_allow_html=True)
#     with back_col:
#         if st.button("← Back to Dashboard", use_container_width=True):
#             st.session_state.page = "dashboard"
#             st.rerun()

#     # Success banner after submit
#     if st.session_state.get("campaign_submitted"):
#         name = st.session_state.get("submitted_name", "New Campaign")
#         st.markdown(f'<div class="success-banner">✓ Campaign "{name}" created successfully!</div>', unsafe_allow_html=True)
#         st.session_state.campaign_submitted = False

#     # ── Section 1: Campaign Details ───────────────────────────────────────
#     st.markdown('<div class="form-card"><div class="form-section-title">Campaign Details</div>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         campaign_name = st.text_input("Campaign Name *", placeholder="e.g. Panasillies Summer 2026")
#         advertiser = st.selectbox("Advertiser *", ["", "Panasillies", "AirMedia Co.", "SkyAds Global", "Other"])
#         campaign_type = st.selectbox("Campaign Type *", ["", "Banner", "Video", "Pre-roll", "Interstitial", "Export"])
#     with col2:
#         airline_program = st.selectbox("Airline Program", ["", "eXW", "PAL", "ANZ", "SIA", "QFA"])
#         start_date = st.date_input("Start Date")
#         end_date = st.date_input("End Date")
#     st.markdown('</div>', unsafe_allow_html=True)

#     # ── Section 2: Targeting ──────────────────────────────────────────────
#     st.markdown('<div class="form-card"><div class="form-section-title">Targeting</div>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         seat_classes = st.multiselect("Seat Classes", ["Business", "First", "Economy", "Premium Economy"])
#         languages = st.multiselect("Languages", ["English", "Mandarin", "Japanese", "Korean", "Arabic", "French"])
#     with col2:
#         aircraft_types = st.multiselect("Aircraft Types", ["A380", "B777", "A350", "B787", "A320"])
#         video_zones = st.multiselect("Video Zones", ["Seatback", "Overhead", "Portal", "Moving Map"])
#     st.markdown('</div>', unsafe_allow_html=True)

#     # ── Section 3: Additional Settings ───────────────────────────────────
#     st.markdown('<div class="form-card"><div class="form-section-title">Additional Settings</div>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         priority = st.selectbox("Priority", ["Normal", "High", "Urgent"])
#     with col2:
#         status = st.selectbox("Initial Status", ["Draft", "Open", "Pending Review"])
#     notes = st.text_area("Notes / Brief", placeholder="Add any campaign notes or creative brief here...", height=100)
#     st.markdown('</div>', unsafe_allow_html=True)

#     # ── Submit / Cancel ───────────────────────────────────────────────────
#     col_submit, col_cancel, _ = st.columns([1, 1, 4])
#     with col_submit:
#         if st.button("✓ Create Campaign", use_container_width=True):
#             if not campaign_name or not advertiser or not campaign_type:
#                 st.error("Please fill in all required fields (marked with *).")
#             else:
#                 st.session_state.campaign_submitted = True
#                 st.session_state.submitted_name = campaign_name
#                 st.session_state.page = "dashboard"
#                 st.rerun()
#     with col_cancel:
#         if st.button("Cancel", use_container_width=True):
#             st.session_state.page = "dashboard"
#             st.rerun()


# # ══════════════════════════════════════════════════════════════════════════
# # Router
# # ══════════════════════════════════════════════════════════════════════════
# if st.session_state.page == "create_campaign":
#     show_create_campaign()
# else:
#     show_dashboard()