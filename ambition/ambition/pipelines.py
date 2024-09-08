class CompanyItemPipeline:
    
    def process_item(self, item, spider):
        
        # Normalize the company name to title case
        item['company_name'] = item['company_name'].title().strip() if item['company_name'] else None

        # Convert ratings to float
        try:
            item['ratings'] = float(item['ratings'])
        except (ValueError, TypeError):
            item['ratings'] = None

        # Normalize ownership to title case
        item['ownership'] = item['ownership'].title().strip() if item['ownership'] else None

        # Clean up 'nob' (Nature of Business)
        item['nob'] = item['nob'].title().strip() if item['nob'] else None

        # Normalize type of company (toc) to title case
        item['toc'] = item['toc'].title().strip() if item['toc'] else None

        # Clean up CEO name
        item['ceo'] = item['ceo'].title().strip() if item['ceo'] else None

        # Clean up headquarters information
        item['headquarters'] = item['headquarters'].title().strip() if item['headquarters'] else None

        # Extract and normalize founded year
        founded_in = item.get('founded_in')
        if founded_in:
            year, _, age = founded_in.partition('(')
            item['founded_in'] = year.strip() if year else None

        # Clean up contact/corporate number (ccn)
        item['ccn'] = item['ccn'].strip() if item['ccn'] else None

        # Clean up description
        item['description'] = item['description'].strip() if item['description'] else None

        return item
