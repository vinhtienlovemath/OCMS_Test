DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_courses',       # Tên cơ sở dữ liệu bạn đã tạo
        'USER': 'root',      # Tên người dùng MySQL của bạn
        'PASSWORD': '1234',  # Mật khẩu MySQL của bạn
        'HOST': 'localhost',                # Hoặc địa chỉ IP nếu cơ sở dữ liệu không phải là local
        'PORT': '3306',                     # Port mặc định MySQL
    }
}
