import biothings.dataload.uploader as uploader
from dataload.uploader import SnpeffPostUpdateUploader

class CosmicUploader(uploader.DummySourceUploader,SnpeffPostUpdateUploader):

    name = "cosmic"
    __metadata__ = {
            "mapper" : 'observed',
            "assembly" : "hg19",
            "src_meta" : {
                "url" : "http://cancer.sanger.ac.uk/cosmic",
                "license_url" : "http://cancer.sanger.ac.uk/cosmic/license",
                "license_url_short": "https://goo.gl/2tibWa",
                "note": "COSMIC v68 was imported from UCSC database dump. This is the last freely available somatic variants from COSMIC before their licence change."
                }
            }

    @classmethod
    def get_mapping(klass):
        mapping = {
            "cosmic": {
                "properties": {
                    "chrom": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "hg19": {
                        "properties": {
                            "start": {
                                "type": "integer"
                            },
                            "end": {
                                "type": "integer"
                            }
                        }
                    },
                    "tumor_site": {
                        "type": "string"
                    },
                    "cosmic_id": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "mut_nt": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "mut_freq": {
                        "type": "float"
                    },
                    "ref": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    },
                    "alt": {
                        "type": "string",
                        "analyzer": "string_lowercase"
                    }
                }
            }
        }
        return mapping

