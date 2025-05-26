from django.db import models

class Pension(models.Model):
    title = models.CharField(
        max_length=256,
        help_text="all inklusive, bed&breakfast,..",
    )
    description = models.TextField(
        max_length=1256,
        help_text="24 saat herşey dahil hizmeet, import içecekler de dahil",
    )
    class Meta:
        db_table="pension"
        verbose_name="Pension"
        verbose_name_plural="Pensions"

    def __str__(self):
        return str(self.title)
