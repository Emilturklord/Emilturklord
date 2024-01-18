from gnuradio import gr

class PrintBinaryBlock(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='PrintBinaryBlock',
            in_sig=[],
            out_sig=[],
        )

    def work(self, input_items, output_items):
        # Get the input from the binary slicer
        input_port = self.get_input(0)
        input_data = input_port[0]

        # Process each input item (0 or 1) and print to console
        for item in input_data:
            print(f'Received: {item}')

        # Return the number of items processed
        return len(input_data)
