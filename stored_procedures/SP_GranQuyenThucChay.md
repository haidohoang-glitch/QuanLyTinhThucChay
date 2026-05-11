# Stored Procedure: `GranQuyenThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-07 14:55:27.250000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.677000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@EmailFrom` | `nvarchar(100)` | No |
| `@EmailTo` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================



CREATE PROCEDURE [dbo].[GranQuyenThucChay]
	-- Add the parameters for the stored procedure here
	@EmailFrom nvarchar(50),
	@EmailTo nvarchar(50)
AS
BEGIN
	Declare @DmChucDanhREF int, @DmPhongBanREF int, @DmNhomLamViecREF int, @DmBoPhanREF int, @NhanSuQuaTrinhCongTacID int
	
	
	set @NhanSuQuaTrinhCongTacID = (
							select Top 1 B.NhanSuQuaTrinhCongTacID from NhanSuSoYeuLyLichFull A
							inner join NhanSuQuaTrinhCongTac B on A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF 
							where 
							A.Email = @EmailTo
							and B.Active = 1
							)
								
	set @DmChucDanhREF = (
							select Top 1 B.DmChucDanhREF from NhanSuSoYeuLyLichFull A
							inner join NhanSuQuaTrinhCongTac B on A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF 
							where 
							A.Email = @EmailFrom
							and B.Active = 1
							)
	set @DmBoPhanREF = (
							select Top 1 B.DmBoPhanREF from NhanSuSoYeuLyLichFull A
							inner join NhanSuQuaTrinhCongTac B on A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF 
							where 
							A.Email = @EmailFrom
							and B.Active = 1
							)	
							
	set @DmPhongBanREF = (
							select Top 1 B.DmPhongBanREF from NhanSuSoYeuLyLichFull A
							inner join NhanSuQuaTrinhCongTac B on A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF 
							where 
							A.Email = @EmailFrom
							and B.Active = 1
							)	
							
	set @DmNhomLamViecREF = (
							select Top 1 B.DmNhomLamViecREF from NhanSuSoYeuLyLichFull A
							inner join NhanSuQuaTrinhCongTac B on A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF 
							where 
							A.Email = @EmailFrom
							and B.Active = 1
							)		
							
	update NhanSuQuaTrinhCongTac		
	set 
	   DmChucDanhREF = @DmChucDanhREF,
	   DmBoPhanREF = @DmBoPhanREF,
	   DmPhongBanREF = @DmPhongBanREF,
	   DmNhomLamViecREF = @DmNhomLamViecREF
	where NhanSuQuaTrinhCongTacID = @NhanSuQuaTrinhCongTacID
	   																			
	select 
	   DmChucDanhREF ,
	   DmBoPhanREF ,
	   DmPhongBanREF ,
	   DmNhomLamViecREF 
	from NhanSuSoYeuLyLichFull A
	inner join NhanSuQuaTrinhCongTac B on A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF 
	where 
	A.Email = @EmailTo
	and B.Active = 1	   
END

```
