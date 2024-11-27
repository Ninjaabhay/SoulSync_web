# SoulSync: AI-Powered Mental Health Chatbot

SoulSync is a mental health chatbot designed to provide empathetic and helpful conversations. The chatbot uses advanced AI to engage users and offer guidance, making it a great tool for mental wellness support.

---

## **Live Link**

Check out the live version of the chatbot here: [SoulSync Live](https://project-soulsync.onrender.com/)

---

## **Features**

- Friendly and supportive chatbot for mental wellness.
- Real-time, interactive chat interface.
- AI-powered conversational responses.

---

## **Installation**

Follow these steps to set up SoulSync locally:

### **1. Clone the Repository**

```bash
git clone https://github.com/Ninjaabhay/SoulSync_web
cd soulsync
```

### **2. Set Up Environment Variables**

Create a `.env` file in the root directory of the project and add the following configuration:

```plaintext
DEBUG=True
SECRET_KEY='your-secret-key-here'
# DATABASE_URL=postgres://username:password@host:port/dbname
HUGGINGFACE_API_KEY='your-huggingface-api-key-here'
```

#### **Explanation:**

- **`DEBUG`**: Set to `True` for development. For production, set this to `False`.
- **`SECRET_KEY`**: Replace with a strong and unique secret key for your Django project.
- **`DATABASE_URL`**: Uncomment and update if using a PostgreSQL database.
- **`HUGGINGFACE_API_KEY`**: Replace with your Hugging Face API key for BlenderBot or other AI services.

### **3. Install Dependencies**

Ensure Python 3.8+ is installed. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### **4. Run Database Migrations**

```bash
python manage.py migrate
```

### **5. Run the Server**

Start the Django development server:

```bash
python manage.py runserver
```

The project will be accessible at `http://127.0.0.1:8000/`.

---

## **How It Works**

1. Open the chat interface in your browser.
2. Type your queries in the chatbox to interact with the AI-powered chatbot.
3. The chatbot provides empathetic and helpful responses.

---

## **Deployment**

The project can be deployed using [Render](https://render.com/) or similar platforms.

Steps for deployment:

1. Push the code to your GitHub repository.
2. Link your repository to Render or any other hosting service.
3. Configure environment variables as shown in the `.env` setup.
4. Deploy and access the chatbot via the live link.

---

## **Contact**

For queries or support, feel free to reach out:  
📧 **[abhaytiwari.contact@gmail.com](mailto:abhaytiwari.contact@gmail.com)**  
🔗 **[LinkedIn](https://www.linkedin.com/in/tiwari-abhay)**

---

_Happy chatting with SoulSync!_
