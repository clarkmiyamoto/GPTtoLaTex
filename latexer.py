from pylatex import Document, Section, Subsection, Math
from pylatex.utils import NoEscape

class LaTexer:
    '''
    Generates a LaTex document
    '''
    __supported_styles__ = ['section', 'subsection', 'text', 'equation']

    def __init__(self):
        self.doc = None

    def add_section(self, doc, title):
        with doc.create(Section(title)):
            pass

    def add_subsection(self, doc, title):
        with doc.create(Subsection(title)):
            pass

    def add_text(self, doc, text):
        doc.append(text)

    def add_equation(self, doc, equation):
        with doc.create(Math(mode='equation')):
            doc.append(NoEscape(equation))

    def add_package(self, doc, package):
        doc.packages.append(package)

    def check_blocks(self, blocks):
        for key in blocks.keys():
            if key not in self.__supported_styles__:
                raise ValueError(f'All keys in blocks must be: {slef.__supported_styles__}')

    def generate_document(self, title: str, blocks: dict, file_path: str = 'main.pdf'):
        '''
        Main functionality of LaTexer.
        Generates latex document described by title + sections

        Args:
        - title (str)
        - sections (str)

        Returns:
        - doc (pylatex.Document)
        '''
        # Check blocks to see if this is a valid data structure
        self.check_blocks(blocks)

        # Create document object
        doc = Document(title)

        # Add packages
        self.add_package('amsmath')
        self.add_package('amssymb')

        # Add sections and subsections
        for style, content in blocks.items():
            
            if (style == 'section'):
                add_section(doc, content)
            elif (style == 'subsection'):
                add_subsection(doc, content)
            elif (style == 'text'):
                add_text(doc, content)
            elif (style == 'equation'):
                add_equation(doc, content)

        # Update `self.doc`
        self.doc = doc

        # Save to file
        doc.generate_pdf(file_path, clean_tex=True)

        return doc
