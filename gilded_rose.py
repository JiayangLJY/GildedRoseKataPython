# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.base_updator = BaseQualityUpdator()
        self.updator_dict = {
            "Aged Brie": AgedBrieUpdator(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdator(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdator(),
            "Conjured": ConjuredUpdator(),
        }

    def update_quality(self):
        for item in self.items:
            self.updator_dict.get(item.name, self.base_updator).update_quality(item)
            self.check_quality(item)

    def check_quality(self, item: Item):
        '''check if 0 < item.quality < 50'''
        if item.quality < 0:
            item.quality = 0
        if item.quality > 50:
            item.quality = 50

class BaseQualityUpdator:

    def update_quality(self, item: Item):
        '''base method to update item quality'''
        item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality -= 1


class AgedBrieUpdator(BaseQualityUpdator):
    '''Aged Brie actually increases in Quality the older it gets'''

    def update_quality(self, item: Item):
        item.sell_in -= 1
        item.quality += 1


class SulfurasUpdator(BaseQualityUpdator):
    '''Sulfuras, being a legendary item, never has to be sold or decreases in Quality'''

    def update_quality(self, item: Item):
        pass

class BackstagePassesUpdator(BaseQualityUpdator):
    '''Backstage passes, like aged brie, increases in Quality as its SellIn value approaches;
    Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    Quality drops to 0 after the concert'''

    def update_quality(self, item: Item):
        if item.sell_in > 0:
            item.quality += 1
            if item.sell_in < 11:
                    item.quality += 1
            if item.sell_in < 6:
                    item.quality += 1
        else:
            item.quality = 0
        item.sell_in -= 1


class ConjuredUpdator(BaseQualityUpdator):
    '''Conjured items degrade in Quality twice as fast as normal items'''

    def update_quality(self, item: Item):
        item.quality -= 2
        item.sell_in -= 1
