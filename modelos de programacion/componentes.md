
# 📘 Componentes de Software

## Ejemplos con Diagramas y Código en Python

---

# 1. 🧩 Componente de Autenticación

## 📌 Diagrama del Componente

```mermaid
graph LR
    Client[Cliente / UI] --> AuthComponent

    subgraph AuthComponent[«Componente» Autenticación]
        AuthService --> UserRepository
        AuthService --> TokenService
    end
```

---

## 📦 Estructura del Componente

```
auth_component/
 ├── auth_service.py
 ├── token_service.py
 └── user_repository.py
```

---

# 2. 🎓 Componente de Matrícula Estudiantil

## 📌 Diagrama del Componente

```mermaid
graph LR
    UI[Portal Estudiantes] --> EnrollmentComponent

    subgraph EnrollmentComponent[«Componente» Matrícula]
        EnrollmentService --> StudentRepository
        EnrollmentService --> CourseRepository
        EnrollmentService --> EnrollmentPolicy
    end
```

---

## 📦 Estructura del Componente

```
enrollment_component/
 ├── repositories.py
 ├── policy.py
 └── enrollment_service.py
```
