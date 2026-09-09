# 🩸 Blood Donation Management System with AI Chatbot using MCP

## 📌 Project Overview

The Blood Donation Management System is a web-based application developed using Python and Streamlit to simplify blood donor management, blood inventory tracking, emergency blood requests, and hospital management. The system also integrates an AI-powered chatbot using the Google Gemini API to provide users with instant information related to blood donation.

The project demonstrates the use of the **Model Context Protocol (MCP)** by connecting an MCP server with an AI client, enabling the chatbot to access and utilize application resources in a structured manner.

---

# 🎯 Objectives

- Manage blood donor information efficiently.
- Maintain blood inventory records.
- Process emergency blood requests.
- Manage hospital information.
- Display nearby hospitals.
- Provide AI assistance using the Gemini API.
- Demonstrate MCP Server integration with an AI application.

---

# 🚀 Features

## 👥 Donor Management
- Register new blood donors
- Store donor details in SQLite database
- View all registered donors

## 🩸 Blood Inventory
- Add blood stock
- Update available units
- Display current inventory

## 🚨 Emergency Blood Request
- Check blood availability
- Display matching donors if stock is insufficient

## 🏥 Hospital Management
- Manage hospital information
- Store hospital records

## 🗺️ Nearby Hospitals
- Display nearby hospitals
- Show hospital locations on an interactive map

## 🤖 AI Chatbot
- Built using Google Gemini API
- Answers blood donation related questions
- Maintains chat history during the session
- Accessible directly from the home page

---

# 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- Google Gemini API
- Model Context Protocol (MCP)
- dotenv
- Pandas

---

# 📂 Project Structure

```
BloodDonation/
│
├── app.py
├── database.py
├── .env
├── requirements.txt
│
├── screens/
│   ├── home.py
│   ├── chatbot.py
│   ├── add_donor.py
│   ├── view_donors.py
│   ├── blood_inventory.py
│   ├── emergency_request.py
│   ├── hospital_management.py
│   └── nearby_hospitals.py
│
├── services/
│   ├── donor_service.py
│   ├── inventory_service.py
│   ├── emergency_service.py
│   ├── hospital_service.py
│   ├── dashboard_service.py
│   ├── notification_service.py
│   └── map_service.py
│
└── data/
    └── bloodbank.db
```

---

# 🤖 AI Chatbot Integration

The AI chatbot is developed using the **Google Gemini API**.

The chatbot can:

- Answer blood donation queries
- Explain blood groups
- Provide donor eligibility information
- Explain emergency blood requests
- Answer general healthcare questions

The chatbot maintains conversation history throughout the session.

---

# 🔗 MCP Server Integration

This project also demonstrates the use of the **Model Context Protocol (MCP)**.

### What is MCP?

The Model Context Protocol (MCP) is an open standard that enables AI models to securely communicate with external tools, databases, and applications.

### How MCP is used in this project

- An MCP Server was created for the Blood Donation Management System.
- The MCP Server exposes application resources and functionality.
- The server was connected to an AI client (Claude Desktop) for testing.
- The AI client can access project data through the MCP Server.
- This demonstrates how AI assistants can interact with external applications using a standardized protocol.

---

# 🗄️ Database

SQLite is used as the backend database.

Main tables include:

- Donors
- Blood Inventory
- Hospitals

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/SRITHU2007/Blood-Donation-Management-System.git
```

Move into the project folder:

```bash
cd Blood-Donation-Management-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

# 📊 Modules

- Home Dashboard
- Donor Registration
- View Donors
- Blood Inventory
- Emergency Blood Request
- Hospital Management
- Nearby Hospitals
- AI Chatbot

---

# 💡 Future Enhancements

- User Authentication
- Blood Request Notifications
- Email and SMS Alerts
- Cloud Database Integration
- Real-time Hospital Updates
- Voice-enabled AI Chatbot
- Mobile Application
- Appointment Scheduling