from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management import call_command


class Command(RunserverCommand):
    help = 'Starts a lightweight Web server for development and optionally re-embeds documents before start.'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--embed',
            action='store_true',
            dest='embed',
            help='Re-embed documents before starting the server',
        )
        parser.add_argument(
            '--embed-device',
            type=str,
            default='cpu',
            dest='embed_device',
            help='Device for embedding (cpu|cuda)',
        )
        parser.add_argument(
            '--embed-docs',
            type=str,
            default=None,
            dest='embed_docs',
            help='Override documents path for embedding',
        )
        parser.add_argument(
            '--embed-out',
            type=str,
            default=None,
            dest='embed_out',
            help='Override output path for saved embeddings',
        )

    def handle(self, *args, **options):
        if options.get('embed'):
            kwargs = {}
            if options.get('embed_device'):
                kwargs['device'] = options['embed_device']
            if options.get('embed_docs'):
                kwargs['docs'] = options['embed_docs']
            if options.get('embed_out'):
                kwargs['out'] = options['embed_out']
            self.stdout.write(self.style.NOTICE('Re-embedding documents before starting server...'))
            call_command('reembed_documents', **kwargs)
            self.stdout.write(self.style.SUCCESS('Re-embedding complete.'))

        return super().handle(*args, **options)


