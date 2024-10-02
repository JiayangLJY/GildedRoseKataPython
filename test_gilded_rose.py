# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_quality_not_negative(self):
        '''The Quality of an item is never negative'''
        item_name = "negative_quality"
        items = [Item(item_name, 1, 2), Item(item_name, 1, 1), Item(item_name, 1, 0), ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items == [Item(item_name, 0, 1), Item(item_name, 0, 0), Item(item_name, 0, 0)]


    def test_quality_less_than_50(self):
        '''The Quality of an item is never more than 50'''
        item_name = "expensive_item"
        items = [Item(item_name, 1, 2), Item(item_name, 9, 19), Item(item_name, 4, 55), ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items == [Item(item_name, 0, 1), Item(item_name, 8, 18)]

    def test_aged_brice(self):
        ''' "Aged Brie" actually increases in Quality the older it gets'''
        init_quality = 20
        items = [Item("NOT Aged Brie", 10, init_quality)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items[0].quality > init_quality



if __name__ == '__main__':
    unittest.main()
