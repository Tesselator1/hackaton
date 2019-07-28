from django.db import models


class SupplyDocument(models.Model):
    docNum = models.CharField(verbose_name="Номер", max_length=20)
    docDate = models.DateField(verbose_name="Дата", auto_now_add=True)
    docSupplier = models.CharField(verbose_name="Поставщик", max_length=100)


class Part(models.Model):
    name = models.CharField(max_length=100, unique=True)
    attached = models.ManyToManyField("self", through="Membership", symmetrical=False)


class Membership(models.Model):
    from_part = models.ForeignKey('Part', related_name='from_parts', on_delete=models.CASCADE)
    to_part = models.ForeignKey('Part', related_name='to_parts', on_delete=models.CASCADE)
    count_part = models.IntegerField(default=1)

    class Meta:
        unique_together = ('from_part', 'to_part')


class ProducedPart(models.Model):
    super = models.ForeignKey(Part, on_delete=models.CASCADE)
    params = models.CharField(max_length=200)
    docs = models.ManyToManyField(SupplyDocument)
