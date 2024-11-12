using EmployeeHelper.Domain;
using EmployeeHelper.Infrastructure.DataAccess;
using Microsoft.AspNetCore.Identity;

namespace EmployeeHelper.Initializers;

public static class IdentityInitializer
{
    public static void AddIdentity(IServiceCollection services)
    {
        services.AddIdentity<User, Role>()
            .AddEntityFrameworkStores<AppDbContext>()
            .AddDefaultTokenProviders();

        services.Configure<IdentityOptions>(o => o.Password.RequireNonAlphanumeric = false);
    }
}
