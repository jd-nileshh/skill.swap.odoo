# SkillSwap

SkillSwap is a Django-based web application that allows users to exchange skills with one another. Whether you're a developer interested in learning photography or a chef curious about digital marketing, SkillSwap connects users who are ready to share and learn.

---

## Features

- Custom user model (`SwapUser`) with fields like name, email, city, skills offered, and skills wanted
- Profile image upload support
- Clean and responsive black-and-white themed UI
- Request button for each user card to initiate skill exchange
- Easily extendable architecture for chat, matching, or notifications

---

## Tech Stack

- Backend: Django 5.1+
- Frontend: HTML, CSS (inline styling for now)
- Database: SQLite (default)
- Authentication: Django’s built-in auth with a custom user model
- Media: Django media files (for profile image uploads)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/skillswap.git
cd skillswap
