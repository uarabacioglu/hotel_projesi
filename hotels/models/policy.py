from django.db import models


class Policy(models.Model):
    title = models.CharField(
        max_length=256,
        help_text="check-in 14:00",
    )

    class Meta:
        db_table = "policies"
        verbose_name = "Policy"
        verbose_name_plural = "Policies"

    def __str__(self):
        return str(self.title)
