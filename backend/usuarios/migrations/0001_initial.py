import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Comuna",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="EstadoCot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Extra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
                ("recargo", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="MetodoPago",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
                ("sigla", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Reserva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("porcentaje", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Rol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
                ("permisos", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("rut", models.CharField(max_length=12, unique=True)),
                ("dv", models.CharField(max_length=1)),
                ("direccion", models.CharField(max_length=255)),
                ("telefono", models.CharField(max_length=15)),
                ("correo", models.EmailField(max_length=254)),
                ("contrasena", models.CharField(max_length=128)),
                (
                    "comuna",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.comuna",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.region",
                    ),
                ),
                (
                    "rol",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.rol",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cotizacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("detalle_venta", models.TextField()),
                ("fecha", models.DateField()),
                ("subtotal", models.IntegerField()),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.cliente",
                    ),
                ),
                (
                    "estado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.estadocot",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("razon_social", models.CharField(max_length=100)),
                ("categoria", models.CharField(max_length=100)),
                ("rut", models.CharField(max_length=12, unique=True)),
                ("dv", models.CharField(max_length=1)),
                ("direccion", models.CharField(max_length=255)),
                ("telefono", models.CharField(max_length=15)),
                ("correo", models.EmailField(max_length=254)),
                (
                    "comuna",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.comuna",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.region",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="comuna",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="usuarios.region"
            ),
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("rut", models.CharField(max_length=12, unique=True)),
                ("dv", models.CharField(max_length=1)),
                ("direccion", models.CharField(max_length=255)),
                ("telefono", models.CharField(max_length=15)),
                ("correo", models.EmailField(max_length=254)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
                (
                    "comuna",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.comuna",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.region",
                    ),
                ),
                (
                    "rol",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.rol",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Servicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
                ("precio", models.IntegerField()),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.categoria",
                    ),
                ),
                (
                    "extra",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="usuarios.extra",
                    ),
                ),
                (
                    "proveedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.proveedor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripcion", models.CharField(max_length=100)),
                ("aforo", models.IntegerField()),
                ("fecha", models.DateField()),
                ("hora", models.TimeField()),
                ("estado", models.CharField(max_length=50)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.categoria",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.cliente",
                    ),
                ),
                (
                    "comuna",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.comuna",
                    ),
                ),
                (
                    "servicio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.servicio",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Venta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("subtotal", models.IntegerField()),
                ("iva", models.IntegerField()),
                ("total", models.IntegerField()),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.cliente",
                    ),
                ),
                (
                    "cotizacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.cotizacion",
                    ),
                ),
                (
                    "metodo_pago",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.metodopago",
                    ),
                ),
            ],
        ),
    ]
