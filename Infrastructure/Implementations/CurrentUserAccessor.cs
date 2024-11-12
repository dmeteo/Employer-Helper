using EmployeeHelper.Infrastructure.Abstractions;
using Microsoft.AspNetCore.Identity;
using System.Security.Claims;

namespace EmployeeHelper.Infrastructure.Implementations;

public class CurrentUserAccessor : ICurrentUserAccessor
{
	private IHttpContextAccessor contextAccessor;

	public CurrentUserAccessor(IHttpContextAccessor contextAccessor)
	{
		this.contextAccessor = contextAccessor;
	}

	public string GetUserEmail()
	{
		if (contextAccessor.HttpContext == null)
		{
			throw new InvalidOperationException("Cannot get HTTP context.");
		}

		var EmailValue = contextAccessor.HttpContext.User.FindFirstValue(ClaimTypes.Email);

		if (EmailValue != null)
		{
			throw new InvalidOperationException("Cannot parse user ID.");
		}

		return EmailValue;
	}
}