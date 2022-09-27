tiny project where i try to implement this 'image-paste' feature (just like whatsapp and other webapps do: open web-site, paste an image and the image can be pre-viewed, then sent);

so far, i can already set a 'classic' form with a text field and an image field, easy-peasy

now i'm trying to do as described above, with a custom form;
i tried to do things as described in https://stackoverflow.com/questions/43481931/how-to-upload-an-image-through-copy-paste-using-django-modelform#43502536

the idea is to set a hidden input field where the image goes in text-form... and the image field is shown via a custom widget


got some help there setting up an event handler and all that
...but don't know much javascript yet

so far things work (in the console one can see the paste event and the hidden input field's value set as this string representing the image...)
but i can't submit the form. stuck now. pls help...!
