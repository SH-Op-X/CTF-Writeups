from .image import Image
from .query import Query


class Implication:
    def __init__(self, condition: Query, add_tags: list[str], remove_tags: list[str]):
        self.condition = condition
        self.add_tags = add_tags
        self.remove_tags = remove_tags


class Engine:
    def __init__(self, implications: list[Implication]):
        self.implications = implications
        self.inv_map = {}
        for i, imp in enumerate(implications):
            for tag in imp.condition.tags():
                self.inv_map.setdefault(tag, set()).add(i)
            for tag in imp.add_tags + imp.remove_tags:
                self.inv_map.setdefault(tag, set()).add(i)

    def apply_slow(self, image: Image):
        applied = set()
        while True:
            add_tags = set()
            remove_tags = set()
            for i, imp in enumerate(self.implications):
                if imp.condition.matches(image):
                    if i in applied:
                        # It's guaranteed that the same implication applied
                        # multiple times will not change the result
                        assert image.tags.issuperset(imp.add_tags)
                        assert not (image.tags & imp.remove_tags)
                        continue

                    applied.add(i)
                    add_tags.update(imp.add_tags)
                    remove_tags.update(imp.remove_tags)

            if not add_tags and not remove_tags:
                break

            image.tags.update(add_tags)
            image.tags -= set(remove_tags)

    # Optimized version, same functionality
    def apply(self, image: Image):
        imps = range(len(self.implications))
        rounds = 0
        while imps:
            print(rounds)
            add_tags = set()
            remove_tags = set()
            for i in imps:
                imp = self.implications[i]
                if imp.condition.matches(image):
                    add_tags.update(imp.add_tags)
                    remove_tags.update(imp.remove_tags)

            add_tags -= image.tags
            remove_tags &= image.tags

            imps = set()
            for tag in add_tags | remove_tags:
                imps.update(self.inv_map.get(tag, set()))

            image.tags |= add_tags
            image.tags -= remove_tags
            rounds += 1

        print('Rounds', rounds)

        return image
