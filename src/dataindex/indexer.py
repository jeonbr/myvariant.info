import biothings.dataindex.indexer as indexer


class VariantIndexer(indexer.Indexer):

    def get_mapping(self, enable_timestamp=True):
        mapping = super(VariantIndexer,self).get_mapping(enable_timestamp=enable_timestamp)
        # enrich with myvariant specific stuff
        mapping["properties"]["chrom"] = {
            'analyzer': 'string_lowercase',
            'include_in_all': False,
            'type': 'string'}

        return mapping
