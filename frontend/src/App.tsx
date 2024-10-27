import './App.css';

import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { Button } from './components/ui/button';
import { Input } from './components/ui/input';

const ONE_MB_IN_BYTE = 100000;

const fileLargerThan = (threshold: number) => (file: File) => file.size > threshold;

const formSchema = z.object({
  receipts: z.instanceof(FileList).refine(
    (files) => Array.from(files).some(fileLargerThan(10 * ONE_MB_IN_BYTE)),
    (files) => ({
      message: `Following files are greater than 7MB: ${Array.from(files)
        .filter(fileLargerThan(10 * ONE_MB_IN_BYTE))
        .map((item) => item.name)
        .join(', ')} is greater than 7MB.`,
    }),
  ),
});

function App() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      receipts: undefined,
    },
  });

  // 2. Define a submit handler.
  function onSubmit(values: z.infer<typeof formSchema>) {
    // Do something with the form values.
    // ✅ This will be type-safe and validated.
    console.log(values);
  }

  return (
    <>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
          <FormField
            control={form.control}
            name={`receipts`}
            render={({ field: { value: _, onChange, ...fieldProps } }) => (
              <FormItem>
                <FormLabel>Receipt</FormLabel>
                <FormControl>
                  <Input
                    {...fieldProps}
                    placeholder="Picture"
                    type="file"
                    accept="image/*, application/pdf"
                    multiple
                    onChange={(event) => {
                      console.log(event.target.files);
                      return onChange(event.target.files);
                    }}
                  />
                </FormControl>
                <FormDescription>This is your public display name.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit">Submit</Button>
        </form>
      </Form>
    </>
  );
}

export default App;
