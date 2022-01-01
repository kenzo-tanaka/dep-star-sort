class DependencyPage:
	def __init__(self, url) -> None:
			self.url = url

	def popular_repos(self):
		return(
			[
				{
					'repo': 'https://github.com/ledermann/templatus-hotwire',
					'star': 6,
				},
				{
					'repo': 'https://github.com/ParamagicDev/rails_starter',
					'star': 5
				}
			]
		)
