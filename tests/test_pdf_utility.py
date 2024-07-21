import unittest
from unittest.mock import patch, MagicMock
from main import convert_img_to_pdf, merge_pdfs

class TestPDFUtility(unittest.TestCase):

    @patch('main.Image.open')
    def test_convert_img_to_pdf(self, mock_open):
        # Créer un mock pour l'image ouverte et sa méthode save
        mock_image = MagicMock()
        mock_open.return_value = mock_image

        file_path = 'test_image.png'
        pdf_path = 'test_output.pdf'
        
        result = convert_img_to_pdf(file_path, pdf_path)
        
        mock_open.assert_called_once_with(file_path)
        mock_image.save.assert_called_once_with(pdf_path, "PDF", resolution=100.0)
        self.assertEqual(result, pdf_path)

    @patch('main.PdfMerger')
    def test_merge_pdfs(self, MockPdfMerger):
        files = ['file1.pdf', 'file2.pdf']
        output_path = 'merged_output.pdf'
        
        merger_instance = MockPdfMerger.return_value
        
        result = merge_pdfs(files, output_path)
        
        self.assertEqual(merger_instance.append.call_count, len(files))
        merger_instance.write.assert_called_once_with(output_path)
        merger_instance.close.assert_called_once()
        self.assertEqual(result, output_path)

if __name__ == '__main__':
    unittest.main()
