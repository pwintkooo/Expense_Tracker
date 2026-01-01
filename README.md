# 💰 Expense Tracker App

A modern, web-based expense tracking application built with Flask and SQLAlchemy. Track your expenses with a beautiful, responsive interface featuring soft blue and orange color themes.

![Expense Tracker](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![Flask](https://img.shields.io/badge/flask-2.0+-orange)

## ✨ Features

### 🔐 User Authentication
- **Secure Registration** with email and username
- **Encrypted Passwords** using Flask-Bcrypt hashing
- **Session-based Authentication** for secure user sessions
- **Login/Logout** functionality

### 💳 Expense Management
- **Add Expenses** with title, amount, category, and description
- **Edit Expenses** with inline editing interface
- **Delete Expenses** with confirmation modal
- **View All Expenses** in a clean, organized table
- **Category Management** with preset categories and custom category option
- **Automatic Timestamp Tracking** (created_at) for all expenses

### 🎨 Modern UI/UX
- **Responsive Design** works seamlessly on desktop, tablet, and mobile
- **Modern Color Scheme**:
  - Soft Blues (#6793AC, #8AB1C7)
  - Orange Accents (#E4580B, #FF6D1F)
  - Neutral Dark Text (#2C3E50)
  - Light Background (#F0F4F7)
- **Floating Action Button (FAB)** for quick expense addition
- **Smooth Animations** and hover effects
- **Card-based Layout** with rounded corners and shadows
- **Clean Typography** with proper spacing and hierarchy

### 🔧 Technical Features
- **SQLite Database** with SQLAlchemy ORM
- **Database Migrations** using Flask-Migrate (Alembic)
- **Foreign Key Relationships** for data integrity
- **Flash Messages** for user feedback
- **Form Validation** on both client and server side

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Expense_Tracker_App
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Create a .env file**
   ```bash
   # Create a .env file in the root directory with:
   DATABASE_URL=sqlite:///expenses.db
   SECRET_KEY=your-secret-key-here
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Initialize the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

7. **Run the application**
   ```bash
   python app.py
   ```

8. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:5000`

## 📁 Project Structure

```
Expense_Tracker_App/
│
├── app.py                     # Main Flask application entry point
├── requirements.txt           # Python dependencies
├── vercel.json               # Vercel deployment configuration
├── README.md                 # This file
│
├── backend/                  # Backend logic
│   ├── __init__.py
│   ├── auth_routes.py        # Authentication routes (login, register, logout)
│   ├── expense_routes.py     # Expense CRUD routes
│   └── models.py             # SQLAlchemy database models
│
├── migrations/               # Database migration files
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions/            # Migration versions
│       └── fb4ee8f0cc4f_initial_migration.py
│
└── templates/               # HTML templates
    ├── index.html          # Home page with expense list
    ├── login.html          # Login page
    ├── register.html       # Registration page
    ├── add_expense.html    # Add expense form
    └── edit_expense.html   # Edit expense form
```

## 💻 Usage

### 1. Register an Account
- Navigate to the register page
- Enter your email, username, and password
- Password will be securely hashed before storage
- Click "Register" to create your account

### 2. Login
- Enter your registered email and password
- Click "Login" to access your dashboard

### 3. Add Expense
- Click the **floating orange "+" button** at the bottom-right corner
- Fill in the expense details:
  - Title (required)
  - Amount (required)
  - Category (select from preset or add custom)
  - Description (optional)
- Click "Add Expense" to save

### 4. View Expenses
- All expenses are displayed in a table on the home page
- Expenses are sorted by date (newest first)
- Click any row to edit that expense

### 5. Edit Expense
- Click on any expense row in the table
- Click the "Edit" button to enable editing
- Modify the fields as needed
- Click "Save Changes" to update

### 6. Delete Expense
- In the edit page, click the "Delete" button
- Confirm deletion in the modal dialog
- The expense will be permanently removed

### 7. Logout
- Click the "Logout" button in the top-right corner of the navbar

## 🗄️ Database Schema

### User Table
| Column    | Type    | Constraints           |
|-----------|---------|----------------------|
| user_id   | Integer | Primary Key          |
| email     | String  | Unique, Not Null     |
| userName  | String  | Not Null             |
| password  | String  | Not Null (Hashed)    |

### Expense Table
| Column      | Type     | Constraints              |
|-------------|----------|--------------------------|
| expense_id  | Integer  | Primary Key              |
| title       | String   | Not Null                 |
| amount      | Float    | Not Null                 |
| category    | String   | Not Null                 |
| desc        | String   | Optional                 |
| created_at  | DateTime | Default: Current Time    |
| user_id     | Integer  | Foreign Key (User)       |

## 🛠️ Technologies Used

### Backend
- **Flask 3.1.2** - Web framework
- **SQLAlchemy** - ORM for database management
- **Flask-Migrate** - Database migrations using Alembic
- **Flask-Bcrypt** - Password hashing
- **python-dotenv** - Environment variable management
- **SQLite** - Database

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with custom design system
- **Bootstrap 5.3.3** - Responsive grid and components
- **JavaScript** - Interactive features
- **SVG Icons** - Custom icons

### Development Tools
- **Vercel** - Deployment platform (configured via vercel.json)

## 🔒 Security FeaturesFlask-Bcrypt before storage
- **Session Management**: Secure session-based authentication with Flask sessions
- **SQL Injection Prevention**: Using SQLAlchemy ORM with parameterized queries
- **User Isolation**: Each user can only access their own expenses through user_id foreign key
- **Environment Variables**: Sensitive data stored in .env file (not committed to version control)
- **SQL Injection Prevention**: Using SQLAlchemy ORM with parameterized queries
- **User Isolation**: Each user can only access their own expenses

## 🎨 Design System

### Color Palette
```css
--primary: #6793AC         /* Soft Blue */
--primary-light: #8AB1C7   /* Light Accent Blue */
--secondary: #E4580B       /* Orange Accent */
--secondary-light: #FF6D1F /* Light Orange */
--accent: #114AB1          /* Deep Blue */
--bg-light: #F0F4F7        /* Light Background */
--neutral-dark: #2C3E50    /* Dark Text */
```

### Design Principles
- Modern, clean, minimalistic interface
- Rounded cards (15-20px border-radius)
- Gradients on buttons and headers
- Subtle shadows for depth
- Consistent spacing and typography
- Responsive layout for all screen sizes

## 📱 Responsive Breakpoints

- **Desktop**: > 992px
- **Tablet**: 768px - 992px
- **Mobile**: < 768px

The FAB (Floating Action Button) adjusts size:
- Desktop: 60px × 60px
- Tablet: 56px × 56px
- Mobile: 52px × 52px

## � Deployment

This application is configured for deployment on Vercel using the included `vercel.json` configuration file. The project uses SQLite for local development, but you may need to configure a different database for production (e.g., PostgreSQL) as Vercel has limitations with SQLite persistence.

---

**Made with ❤️ using Flask and Python**
