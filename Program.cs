

using EmployeeHelper.Infrastructure.Abstractions;
using EmployeeHelper.Infrastructure.DataAccess;
using EmployeeHelper.Initializers;

namespace EmployeeHelper;

public class Program
{
	public static void Main(string[] args)
	{
		var builder = WebApplication.CreateBuilder(args);

		ConfigureServices(builder.Services);

		var app = builder.Build();

		using var scope = app.Services.CreateScope();
		using var appDbContext = scope.ServiceProvider.GetRequiredService<AppDbContext>();


		app.UseRouting();

		app.UseAuthentication();
		app.UseAuthorization();

		app.UseStaticFiles();

		app.UseSwagger();
		app.UseSwaggerUI();

		app.MapControllers();
		app.MapDefaultControllerRoute();
		app.MapHealthChecks("health-check");

		app.Run();
	}

	private static void ConfigureServices(IServiceCollection services)
	{
		services.AddHealthChecks();
		services.AddSwaggerGen();

		services.AddAutoMapper(typeof(Program).Assembly);
		services.AddMediatR(o => o.RegisterServicesFromAssembly(typeof(Program).Assembly));

		services.AddAuthentication();
		services.AddAuthorization();
		services.AddControllersWithViews();

		services.AddScoped<IAppDbContext, AppDbContext>();

		IdentityInitializer.AddIdentity(services);
		DbContextInitializer.AddAppDbContext(services);
	}
}