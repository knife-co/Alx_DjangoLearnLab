# 📚 Relationship App – Permissions Setup Guide

This app uses Django’s custom permissions and group system to control access to `Book` model actions.

---

## 🔐 Custom Permissions

Defined in `Book` model's `Meta` class (`models.py`):

| Permission Code | Description        |
|------------------|--------------------|
| `can_view`       | Can view book      |
| `can_create`     | Can create book    |
| `can_edit`       | Can edit book      |
| `can_delete`     | Can delete book    |

---

## 👥 User Groups & Their Permissions

| Group Name | Permissions              |
|------------|--------------------------|
| `Viewers`  | `can_view`               |
| `Editors`  | `can_view`, `can_create`, `can_edit` |
| `Admins`   | All permissions          |

Set these up using Django Admin → `Groups`.

---

## 🧪 Access Control in Views

Django’s `PermissionRequiredMixin` is used in class-based views.

| View               | Permission Required       |
|--------------------|---------------------------|
| `BookListView`     | None                      |
| `BookCreateView`   | `bookshelf.can_create` |
| `BookUpdateView`   | `bookshelf.can_edit`   |
| `BookDeleteView`   | `bookshelf.can_delete` |

---

## 🔐 Authentication

- Login URL: `/accounts/login/`
- Logout URL: `/accounts/logout/`

Make sure users are assigned to the correct group in Django Admin.

---

