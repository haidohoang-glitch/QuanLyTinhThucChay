# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreo_Log`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-23 17:56:07.447000
- **Ngày sửa cuối**: 2021-10-27 17:17:09.727000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreo_Log]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreo_Log]
AS
BEGIN
    DECLARE @NgayThucHien DATETIME;
    DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = '''',
            @LoaiThucTreo_chiphi NVARCHAR(50) = N'';
    SET @NgayThucHien = ISNULL(
                        (
                            SELECT MAX(dchdct.[ThoiGianLog])
                            FROM dbo.ThucChayHopDongChiTietLog dchdct
							WHERE dchdct.InputType = 1
                        ),
                        '2021-06-01'
                              );

	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCTREO' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCTREO' ORDER BY id),'')

    SET @NgayThucHien = DATEADD(HOUR, -1, @NgayThucHien);
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
	[NhanHang] [nvarchar](2000) NULL,
	[BookingREF] [bigint] NULL,
	[ThoiGianBatDau] [date] NULL,
	[ThoiGianKetThuc] [date] NULL,
	[SoLuongThucTreo] [float] NULL,
	[SoLuongThucChay] [float] NULL,
	[DmDonViTinhREF] [int] NULL,
	[DonViTinh] [nvarchar](200) NULL,
	[TypeThucChay] [int] NULL,
	[Link] [nvarchar](2000) NULL,
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
	[DonGia] float,
	[ChietKhau] float
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
		   ,ChietKhau) '
	SET @SQL +=
			'SELECT  [Id]
			,[Contract_Id]
			,[Contract_Detail_Id]
			, 0 as DmBannerID
			,'''' as TenBanner
			, 0 as DmViTriREF
			,'''' as ViTri
			, Dm_NhanHang_id
			, TenNhanHang
			, 0 as BookingREF
			,ThoiGianBatDau as [StartDate]
			,ThoiGianketThuc as [EndDate]
			,SoLuong as [Quantity]
			,SoLuong as [Quantity]
			,DonViTinh_id as [UnitId]
			,'''' as [UnitName]
			, 0 as TypeThucChay
			, LandingPage as Link
			, GhiChu as [Note]
			,[Product_Formality_Id]
			, '''' as product_Fomality_name
			,[Product_Id]
			, '''' as Product_name
			, 1 as Input_type --treo khong phai la chi phi
			, 0 as IsReadBooking
			, [SysEndTime] as ThoiGianLog
			, '''' as NguoiLog
			, 0 LoaiLog
			,[Created_By]
			,[Created_At]
			,[Last_Modified_By]
			,[Last_Modified_At]
			,[Deleted_Status]
			, 0 as PrintStatus
			,0 [RecordStatus]
			, tt.DonGia
			, tt.ChietKhau
		 FROM ' + @server_id + '.' + @database + '.[dbo].[ThucTreo_History] tt
		WHERE 1=1 
		AND tt.[SysEndTime] > ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '

		--PRINT @SQL
		EXEC(@SQL)
		--select * from #ThucChayHopDongChiTietLog

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
		   ,ChietKhau)
 
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
    FROM #ThucChayHopDongChiTietlog dchdct

    DROP TABLE #ThucChayHopDongChiTietlog;

END;


```
