__author__ = "Chris Mitchell"

import os, unittest, hashlib
import pythomics.genomics.parsers as parser


class Test_VCF_Iterator(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.split(__file__)[0]
        data_dir = os.path.join(base_dir, "fixtures")
        self.handle = os.path.join(data_dir, "valid-4.0.vcf")

    def test_vcf_iterator(self):
        f = parser.VCFIterator(self.handle)
        assert isinstance(f, parser.VCFIterator)
        entries = [str(row) for row in f]
        out = "\n".join(entries)
        digest = hashlib.sha224(out.encode("utf-8")).hexdigest()
        self.assertEqual(
            "013ed0dc8b1a1de19d1a2997e95b40b9070c6b1d32f931f568816a0a",
            digest,
            "VCF Iterator Failure",
        )

    def test_vcf_zygosity(self):
        pass

    def test_vcf_variants(self):
        pass

    def test_vcf_filters(self):
        pass

    def test_vcf_alleles(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_VCF_Iterator)
    unittest.TextTestRunner(verbosity=2).run(suite)
