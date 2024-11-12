using EmployeeHelper.Infrastructure.DataAccess;
using Microsoft.EntityFrameworkCore;

namespace EmployeeHelper.Initializers;

public static class DbContextInitializer
{

    public static void AddAppDbContext(IServiceCollection services)
    {
        var pathToDbFile = GetPathToDbFile();

		services
			.AddDbContext<AppDbContext>(options => options
				.UseSqlite($"Data Source={pathToDbFile}"));


		string GetPathToDbFile()
        {
            var applicationFolder = Path.Combine(Environment.GetFolderPath(
              Environment.SpecialFolder.ApplicationData), "EmployeeHelper");

            if (!Directory.Exists(applicationFolder))
            {
                Directory.CreateDirectory(applicationFolder);
            }
            return Path.Combine(applicationFolder, "EmployeeHelper.db");
        }
    }
}
