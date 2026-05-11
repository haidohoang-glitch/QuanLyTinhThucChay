# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreoChiPhi_Log`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-13 16:09:37.527000
- **Ngày sửa cuối**: 2025-04-22 08:56:21.190000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreoChiPhi_Log]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreoChiPhi_Log]
AS
BEGIN
    DECLARE @NgayThucHien DATETIME;
    DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = '''',
            @LoaiThucTreo_chiphi NVARCHAR(50) = N'ChiPhi';
    SET @NgayThucHien = ISNULL(
                        (
                            SELECT MAX(dchdct.[ThoiGianLog])
                            FROM dbo.ThucChayHopDongChiTietLog dchdct
							WHERE dchdct.LoaiThucTreo = N'ChiPhi'
                        ),
                        '1900-01-01'
                              );
	SET @server_id =
	(SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCTREO' ORDER BY id)

	SET @database= 
	(SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCTREO' ORDER BY id)

    SET @NgayThucHien = DATEADD(HOUR, -8, @NgayThucHien);
    --SET @NgayThucHien = '2009-01-01'

    PRINT @NgayThucHien;


CREATE TABLE #ThucChayHopDongChiTietLog(
	[ThucChayHopDongChiTietID] [bigint] NULL,
	[HopDongREF] [bigint] NULL,
	[HopDongChiTietREF] [bigint] NULL,
	[DmBannerREF] [nvarchar](200) NULL,
	[TenBanner] [nvarchar](200) NULL,
	[DmViTriREF] [int] NULL,
	[ViTri] [nvarchar](200) NULL,
	[DmNhanHangREF] [nvarchar](200) NULL,
	[NhanHang] [nvarchar](200) NULL,
	[BookingREF] [bigint] NULL,
	[ThoiGianBatDau] [date] NULL,
	[ThoiGianKetThuc] [date] NULL,
	[SoLuongThucTreo] [float] NULL,
	[SoLuongThucChay] [float] NULL,
	[DmDonViTinhREF] [int] NULL,
	[DonViTinh] [nvarchar](200) NULL,
	[TypeThucChay] [int] NULL,
	[Link] [nvarchar](200) NULL,
	[GhiChu] [nvarchar](max) NULL,
	[DmHinhThucQuangCaoREF] [int] NULL,
	[TenHinhThucQuangCao] [nvarchar](200) NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](200) NULL,
	[InputType] [int] NULL,
	[IsReadBooking] [int] NULL,
	[ThoiGianLog] [datetime] NULL,
	[NguoiLog] [nvarchar](200) NULL,
	[LoaiLog] [int] NULL,
	[CreatedBy] [nvarchar](200) NULL,
	[CreatedAt] [datetime] NULL,
	[LastModifiedBy] [nvarchar](200) NULL,
	[LastModifiedAt] [datetime] NULL,
	[DeletedStatus] [int] NULL,
	[PrintStatus] [int] NULL,
	[RecordStatus] [int] NULL,
	DonGia float,
	ChietKhau float,
	DmWebsiteREF int,
	TenWebsite nvarchar(200),
	TrangThaiTreo int null
)


SET @SQL =
'INSERT INTO #ThucChayHopDongChiTietLog
           ([ThucChayHopDongChiTietID]
           ,[HopDongREF]
           ,[HopDongChiTietREF]
           ,[DmBannerREF]
           ,[TenBanner]
           ,[DmViTriREF]
           ,[ViTri]
           ,[DmNhanHangREF]
           ,[NhanHang]
           ,[BookingREF]
           ,[ThoiGianBatDau]
           ,[ThoiGianKetThuc]
           ,[SoLuongThucTreo]
           ,[SoLuongThucChay]
           ,[DmDonViTinhREF]
           ,[DonViTinh]
           ,[TypeThucChay]
           ,[Link]
           ,[GhiChu]
           ,[DmHinhThucQuangCaoREF]
           ,[TenHinhThucQuangCao]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[InputType]
           ,[IsReadBooking]
           ,[ThoiGianLog]
           ,[NguoiLog]
           ,[LoaiLog]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
           ,[DeletedStatus]
           ,[PrintStatus]
           ,[RecordStatus]
		   ,DonGia
		   ,ChietKhau
		   ,DmWebsiteREF
	       ,TenWebsite
		   ,TrangThaiTreo) '
    
	SET @SQL +=
			'SELECT [Id]
			,[Contract_Id]
			,[Contract_Detail_Id]
			, 0 as DmBannerID
			,'''' as TenBanner
			, 0 as DmViTriREF
			,'''' as ViTri
			,[Brand_Id]
			,[Brand_Name]
			, 0 as BookingREF
			,[StartDate]
			,[EndDate]
			,[Quantity]
			,[Quantity]
			,[UnitId]
			,[UnitName]
			, 0 as TypeThucChay
			, '''' as Link
			,[Note]
			,[Product_Formality_Id]
			, '''' as product_Fomality_name
			,[Product_Id]
			, '''' as Product_name
			, 0 as Input_type
			, 0 as IsReadBooking
			, [SysEndTime] as ThoiGianLog
			, '''' as NguoiLog
			, 0 LoaiLog
			,[CreatedBy]
			,[CreatedAt]
			,[LastModifiedBy]
			,[LastModifiedAt]
			,[DeletedStatus]
			, 0 as PrintStatus
			,[RecordStatus]
			, tt.UnitPrice as DonGia
			, tt.Discount as ChietKhau
			,tt.website_id
			,tt.website_name
			, [RecordStatus]
		FROM ' + @server_id + '.' + @database + '.[dbo].[ThucTreo_ChiPhi_History] tt
		WHERE 1=1 
		AND tt.[SysEndTime] > ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '

		--PRINT @SQL
		EXEC(@SQL)

		--UPDATE WEBSITE
		UPDATE #ThucChayHopDongChiTietLog
		SET DmWebsiteREF = ISNULL(DmWebsiteREF,265),
		TenWebsite = ISNULL(TenWebsite,N'(Blanks)')
		WHERE DmWebsiteREF IS NULL
		

		INSERT INTO [dbo].[ThucChayHopDongChiTietLog]
           ([ThucChayHopDongChiTietID]
           ,[HopDongREF]
           ,[HopDongChiTietREF]
           ,[DmBannerREF]
           ,[TenBanner]
           ,[DmViTriREF]
           ,[ViTri]
           ,[DmNhanHangREF]
           ,[NhanHang]
           ,[BookingREF]
           ,[ThoiGianBatDau]
           ,[ThoiGianKetThuc]
           ,[SoLuongThucTreo]
           ,[SoLuongThucChay]
           ,[DmDonViTinhREF]
           ,[DonViTinh]
           ,[TypeThucChay]
           ,[Link]
           ,[GhiChu]
           ,[DmHinhThucQuangCaoREF]
           ,[TenHinhThucQuangCao]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[InputType]
           ,[IsReadBooking]
           ,[ThoiGianLog]
           ,[NguoiLog]
           ,[LoaiLog]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
           ,[DeletedStatus]
           ,[PrintStatus]
           ,[RecordStatus]
		   ,[LoaiThucTreo]
		   ,DonGia
		   ,ChietKhau
		   ,DmWebsiteREF
		   ,TenWebsite
		   ,TrangThaiTreo)
 
    SELECT  [ThucChayHopDongChiTietID]
           ,[HopDongREF]
           ,[HopDongChiTietREF]
           ,[DmBannerREF]
           ,[TenBanner]
           ,[DmViTriREF]
           ,[ViTri]
           ,[DmNhanHangREF]
           ,[NhanHang]
           ,[BookingREF]
           ,[ThoiGianBatDau]
           ,[ThoiGianKetThuc]
           ,[SoLuongThucTreo]
           ,[SoLuongThucChay]
           ,[DmDonViTinhREF]
           ,[DonViTinh]
           ,[TypeThucChay]
           ,[Link]
           ,[GhiChu]
           ,[DmHinhThucQuangCaoREF]
           ,[TenHinhThucQuangCao]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[InputType]
           ,[IsReadBooking]
           ,[ThoiGianLog]
           ,[NguoiLog]
           ,[LoaiLog]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
           ,[DeletedStatus]
           ,[PrintStatus]
           ,[RecordStatus]
		   ,@LoaiThucTreo_chiphi
		   ,DonGia
		   ,ChietKhau
		   ,DmWebsiteREF
		   ,TenWebsite
		   ,TrangThaiTreo
    FROM #ThucChayHopDongChiTietlog dchdct

    DROP TABLE #ThucChayHopDongChiTietlog;

END;


```
