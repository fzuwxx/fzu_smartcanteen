# Generated by Django 4.2.7 on 2023-12-04 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "customer_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="顾客编号"
                    ),
                ),
                ("customer_name", models.CharField(max_length=20, verbose_name="顾客昵称")),
                (
                    "customer_password",
                    models.CharField(max_length=20, verbose_name="顾客密码"),
                ),
                ("studentID", models.CharField(max_length=20, verbose_name="学号")),
                ("campus", models.CharField(max_length=20, verbose_name="所属校区")),
                ("customer_tel", models.CharField(max_length=11, verbose_name="顾客电话")),
                ("table_numbers", models.CharField(max_length=20, verbose_name="桌号")),
                (
                    "customer_status",
                    models.IntegerField(
                        choices=[(0, "离线"), (1, "在线")], default=0, verbose_name="顾客状态"
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
            options={
                "verbose_name": "用户信息",
                "verbose_name_plural": "用户信息",
                "db_table": "customer",
                "ordering": ["customer_id"],
            },
        ),
    ]